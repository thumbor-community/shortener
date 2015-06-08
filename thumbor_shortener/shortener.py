# -*- coding: utf-8 -*-


class Shortener(object):

    def get(self, key):
        '''
        Get the url assigned to the key.

        :param key: string
        :return:
        :rtype: string
        '''

        # TODO Use a backend to fetch the value of key.
        # ex: backend.get(key). Backends should be abstracted to support
        # different storages (SQL, Redis, Memcache, Riak, etc. )
        pass

    def put(self, key, url):
        '''
        Store the url
        :param key:
        :param url:
        '''

        # TODO Use a backend to store the value of key + url
        
        pass
