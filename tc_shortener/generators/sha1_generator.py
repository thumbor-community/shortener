# -*- coding: utf-8 -*-

# Copyright (c) 2015, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

import hashlib

from tc_shortener.generators import BaseGenerator


class Generator(BaseGenerator):

    def __init__(self, context):
        super(Generator, self).__init__(context)

    def shorten(self, url):
        '''
        :param url: A url to be shortened.
        :return: SHA-1 hex of the url
        :rtype: string
        '''

        return hashlib.sha1(url).hexdigest()
