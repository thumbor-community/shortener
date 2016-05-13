# -*- coding: utf-8 -*-

# Copyright (c) 2016, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

import os.path
import tornado.gen as gen
import tornado.web
import urlparse
import json

from thumbor.handlers.imaging import ImagingHandler
from thumbor.utils import logger

from tc_shortener.shortener import Shortener
from tc_core.web import RequestParser


class UrlShortenerHandler(ImagingHandler):

    should_return_image = True

    @classmethod
    def regex(cls):
        '''
        :return: The regex used for routing.
        :rtype: string
        '''
        return r'/shortener/?(?P<key>.+)?'

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
        self.should_return_image = False

        content_type = self.request.headers.get("Content-Type", '')

        if 'key' in kwargs and kwargs['key']:
            url = kwargs['key']
        elif content_type.startswith("application/json"):
            data = json.loads(self.request.body)
            url = data['url'] if 'url' in data else None
        else:
            url = self.get_body_argument('url', None)

        if not url:
            logger.error("Couldn't find url param in body or key in URL...")
            raise tornado.web.HTTPError(400)

        options = RequestParser.path_to_parameters(url)

        yield self.check_image(options)

        # We check the status code, if != 200 the image is incorrect, and we shouldn't store the key
        if self.get_status() == 200:
            logger.debug("Image is checked, clearing the response before trying to store...")
            self.clear()
            try:
                shortener = Shortener(self.context)
                key = shortener.generate(url)
                shortener.put(key, url)

                self.write(json.dumps({'key': key}))
                self.set_header("Content-Type", "application/json")
            except Exception as e:
                logger.error("An error occurred while trying to store shortened URL: {error}.".format(error=e.message))
                self.set_status(500)
                self.write(json.dumps({'error': e.message}))

    @gen.coroutine
    def execute_image_operations(self):
        if self.should_return_image:
            super(UrlShortenerHandler, self).execute_image_operations()
