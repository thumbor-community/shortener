# -*- coding: utf-8 -*-
import hashlib

from tc_shortener.generators import BaseGenerator


class Generator(BaseGenerator):

    def get(self, url):
        '''
        :param url: A url to be shortened.
        :return: SHA-256 hex of the url
        :rtype: string
        '''

        return hashlib.sha256(url).hexdigest()
