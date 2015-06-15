# -*- coding: utf-8 -*-


class BaseStorage(object):

    def __init__(self, context):
        '''
        :param context: CommunityContext instance
        '''

        self.context = context
