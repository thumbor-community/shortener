# -*- coding: utf-8 -*-

# Copyright (c) 2015, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

import shortuuid as shortuuid

from tc_shortener.generators import BaseGenerator

class Generator(BaseGenerator):

    def __init__(self, context):
        super(Generator, self).__init__(context)

    def shorten(self, url):
        '''
        :param url: A url to be shortened.
        :return: Short UUID for given URL
        :rtype: string
        '''

        return shortuuid.uuid(url)
