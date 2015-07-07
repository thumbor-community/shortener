# -*- coding: utf-8 -*-

# Copyright (c) 2015, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from pyvows import Vows, expect

from tc_shortener.generators.sha256_generator import Generator

from tc_core.context import Context
from thumbor.config import Config
from thumbor.importer import Importer

@Vows.batch
class Sha256GeneratorVows(Vows.Context):
    class ASha256Generator(Vows.Context):
        def topic(self):
            config   = Config()
            importer = Importer(config)

            context = Context(None, config, importer)

            return Generator(context)

        class WhenShortening(Vows.Context):
            def topic(self, sha256_generator):
                return sha256_generator.get('/unsafe/200x300/image.jpg')

            def should_be_hexa(self, topic):
                expect(topic).to_match(r'^[a-f0-9]{64}/image.jpg$')
