# -*- coding: utf-8 -*-

import logging

from redis import Redis, RedisError

from thumbor.utils import on_exception
from tornado.concurrent import return_future

from tc_shortener.storages import BaseStorage

logger = logging.getLogger('thumbor')


class Storage(BaseStorage):

    storage = None

    def __init__(self, context, shared_client=True):
        '''Initialize the RedisStorage

        :param thumbor.context.Context context: Current context
        :param boolean shared_client: When set to True a singleton client will
                                      be used.
        '''

        super(Storage, self).__init__(context)

        self.shared_client = shared_client
        self.storage = self.reconnect_redis()

    def get_storage(self):
        '''Get the storage instance.

        :return Redis: Redis instance
        '''

        if self.storage:
            return self.storage
        self.storage = self.reconnect_redis()

        return self.storage

    def reconnect_redis(self):
        if self.shared_client and Storage.storage:
            return Storage.storage

        password = self.context.config.get(
            'SHORTENER_REDIS_STORAGE_SERVER_PASSWORD',
            None
        )

        storage = Redis(
            port=self.context.config.SHORTENER_REDIS_STORAGE_SERVER_PORT,
            host=self.context.config.SHORTENER_REDIS_STORAGE_SERVER_HOST,
            db=self.context.config.SHORTENER_REDIS_STORAGE_SERVER_DB,
            password=password
        )

        if self.shared_client:
            Storage.storage = storage
        return storage

    def on_redis_error(self, fname, exc_type, exc_value):
        '''Callback executed when there is a redis error.

        :param string fname: Function name that was being called.
        :param type exc_type: Exception type
        :param Exception exc_value: The current exception
        :returns: Default value or raise the current exception
        '''

        if self.shared_client:
            Storage.storage = None
        else:
            self.storage = None

        raise exc_value

    @on_exception(on_redis_error, RedisError)
    def put(self, key, url):
        storage = self.get_storage()
        storage.set(key, url)

    @return_future
    def get(self, key, callback):
        @on_exception(self.on_redis_error, RedisError)
        def wrap():
            return self.get_storage().get(key)

        callback(wrap())
