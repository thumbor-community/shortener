# -*- coding: utf-8 -*-

# Copyright (c) 2015, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

import re

from thumbor.url import Url

class BaseGenerator(object):

    def __init__(self, context):
        self.context = context

    def shorten(self, url):
        pass

    def get(self, url):
        url = url.encode('utf-8')
        image = ""

        if self.context.config.get('SHORTENER_GENERATOR_PRESERVE_NAME'):
            reg = re.compile(Url.regex())
            result = reg.match(url)

            if result == None:
                raise ValueError("URL does not match thumbor's URL pattern")

            result = result.groupdict()

            image = "/{image}".format(image = result['image'])

        return "{hash}{image}".format(
            hash=self.shorten(url),
            image=image
        )
