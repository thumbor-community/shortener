# -*- coding: utf-8 -*-

# Copyright (c) 2015, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.


from tc_core import Extension, Extensions
from tc_shortener.handlers.shortener import UrlShortenerHandler

extension = Extension('shortener')

# Register the required modules
extension.add_module(
    config_key='SHORTENER_GENERATOR',
    class_name='Generator',
    multiple=False
)

extension.add_module(
    config_key='SHORTENER_STORAGE',
    class_name='Storage',
    multiple=False
)

# Register the route
extension.add_handler(UrlShortenerHandler.regex(), UrlShortenerHandler)

Extensions.register(extension)
