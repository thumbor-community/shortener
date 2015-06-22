# -*- coding: utf-8 -*-

# Copyright (c) 2015, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from derpconf.config import Config

from tc_core import Extension, Extensions
from tc_shortener.handlers.shortener import UrlShortenerHandler

extension = Extension('tc_shortener')

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

Config.define('SHORTENER_GENERATOR', 'tc_shortener.generators.sha256_generator', 'Shortened URL generator class.', 'Shortener')
Config.define('SHORTENER_STORAGE',   'tc_shortener.storages.redis_storage',      'Shortened URL storage.',         'Shortener')


Config.define('SHORTENER_REDIS_STORAGE_SERVER_HOST',     'localhost', 'Redis hostname.',           'Shortener')
Config.define('SHORTENER_REDIS_STORAGE_SERVER_PORT',     6379,        'Redis port.',               'Shortener')
Config.define('SHORTENER_REDIS_STORAGE_SERVER_PASSWORD', None,        'Redis password.',           'Shortener')
Config.define('SHORTENER_REDIS_STORAGE_SERVER_DB',       0,           'Redis db name (optional).', 'Shortener')

# Register the route
extension.add_handler(UrlShortenerHandler.regex(), UrlShortenerHandler)

Extensions.register(extension)
