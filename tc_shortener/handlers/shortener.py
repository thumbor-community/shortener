# -*- coding: utf-8 -*-

# Copyright (c) 2015, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

import os.path
import tornado.gen as gen
import tornado.web
import urlparse
import json

from thumbor.handlers.imaging import ImagingHandler

from tc_shortener.shortener import Shortener
from tc_core.web import RequestParser


class UrlShortenerHandler(ImagingHandler):

    @classmethod
    def regex(cls):
        '''
        :return: The regex used for routing.
        :rtype: string
        '''
        return r'/shortener/(?P<key>.+)?'

    @gen.coroutine
    def get(self, **kwargs):

        shortener = Shortener(self.context)

        # Get the url from the shortener and parse the values.
        url = yield gen.maybe_future(shortener.get(kwargs['key']))

        if not url:
            raise tornado.web.HTTPError(404)

        # Patch the request uri to allow normal thumbor operations
        self.request.uri = urlparse.urlparse(url).path

        options = RequestParser.path_to_parameters(self.request.uri)

        name = os.path.basename(options.get('image', None))
        if name:
            self.set_header(
                'Content-Disposition',
                'inline; filename="{name}"'.format(
                    name=name
                )
            )

        # Call the original ImageHandler.get method to serve the image.
        super(UrlShortenerHandler, self).get(**options)

    @gen.coroutine
    def post(self, **kwargs):

        # URL can be passed as a URL argument or in the body
        url = kwargs['url'] if 'url' in kwargs else kwargs['key']

        if not url:
            raise tornado.web.HTTPError(404)

        options = RequestParser.path_to_parameters(url)

        self.check_image(options)

        # We check the status code, if != 200 the image is incorrect, and we shouldn't store the key
        if self.get_status() == 200:
            shortener = Shortener(self.context)
            key = yield gen.maybe_future(shortener.generate(url))
            shortener.put(key, url)

            self.write(json.dumps({'key': key}))
