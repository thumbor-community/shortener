# -*- coding: utf-8 -*-

# Copyright (c) 2015, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from pyvows import Vows, expect

from tc_shortener.generators.short_generator import Generator

from tc_core.context import Context
from thumbor.config import Config
from thumbor.importer import Importer

@Vows.batch
class ShortGeneratorVows(Vows.Context):
    class AShortGenerator(Vows.Context):
        def topic(self):
            config   = Config()
            importer = Importer(config)

            context = Context(None, config, importer)

            return Generator(context)

        class WithIncorrectUrl(Vows.Context):
            @Vows.capture_error
            def topic(self, short_generator):
                return short_generator.get('')

            def should_raise_error(self, topic):
                expect(topic).to_be_an_error_like(ValueError)

        class WhenShortening(Vows.Context):
            def topic(self, short_generator):
                return short_generator.get('/unsafe/200x300/image.jpg')

            def should_preserve_image(self, topic):
                expect(topic).to_match(r'^.*/image.jpg$')

            def should_be_fixed_length(self, topic):
                expect(topic).to_length(22+len('/image.jpg'))