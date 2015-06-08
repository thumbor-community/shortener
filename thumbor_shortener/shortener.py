# -*- coding: utf-8 -*-


class Shortener(object):

    def __init__(self, context):
        '''
        :param context: an instance of `CommunityContext`
        '''

        self.context = context

    def generate(self, url):
        '''
        :param url:
        :return:
        :rtype: string
        '''
        return self.context.modules.shortener_generator.get(url)

    def get(self, key):
        '''
        Get the url assigned to the key.

        :param key: a short url code
        :return:
        :rtype: string
        '''

        return self.context.modules.shortener_backend.get(key)

    def put(self, key, url):
        '''
        Store the url
        :param key:
        :param url:
        '''

        return self.context.modules.shortener_backend.put(key, url)
