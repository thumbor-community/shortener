# -*- coding: utf-8 -*-

from thumbor_shortener.shortener import Shortener
from thumbor.handlers.imaging import ImagingHandler
from thumbor.url import Url

class UrlShortenerHandler(ImagingHandler):

    def get(self, **kwargs):

        # Get the url from the shortener and parse the values.
        url = Shortener.get(self.request.path)
        if not url:
            # TODO Throw a 404
            pass

        options = Url.parse_decrypted(url)

        # Call the original ImageHandler.get method to serve the image.
        super(UrlShortenerHandler, self).get(**options)

