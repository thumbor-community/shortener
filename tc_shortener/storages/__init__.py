# -*- coding: utf-8 -*-

# Copyright (c) 2015, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.


class BaseStorage(object):

    def __init__(self, context):
        '''
        :param context: CommunityContext instance
        '''

        self.context = context
