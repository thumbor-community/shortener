# -*- coding: utf-8 -*-

import re

from thumbor.handlers.imaging import ImagingHandler
from thumbor.url import Url

from thumbor_community.context import Context
from thumbor_shortener.shortener import Shortener


class UrlShortenerHandler(ImagingHandler):

    @classmethod
    def regex(cls):
        '''
        :return: The regex used for routing.
        :rtype: string
        '''
        return '/shortener/(?P<key>.+)'

    def get(self, **kwargs):

        shortener = Shortener(self.context)

        # Get the url from the shortener and parse the values.
        url = shortener.get(kwargs['key'])

        if not url:
            raise tornado.web.HTTPError(404)

        options = Url.parse_decrypted(url)

        # Call the original ImageHandler.get method to serve the image.
        return super(UrlShortenerHandler, self).get(**options)
