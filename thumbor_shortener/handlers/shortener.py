# -*- coding: utf-8 -*-

import os.path
import tornado.gen as gen
import tornado.web
import urlparse

from thumbor.handlers.imaging import ImagingHandler

from thumbor_shortener.shortener import Shortener
from thumbor_community.web import RequestParser


class UrlShortenerHandler(ImagingHandler):

    @classmethod
    def regex(cls):
        '''
        :return: The regex used for routing.
        :rtype: string
        '''
        return r'/shortener/(?P<key>.+)'

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
