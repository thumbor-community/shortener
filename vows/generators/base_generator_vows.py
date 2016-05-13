# -*- coding: utf-8 -*-

# Copyright (c) 2016, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from pyvows import Vows, expect

from tc_shortener.generators import BaseGenerator

from tc_core.context import Context
from thumbor.config import Config
from thumbor.importer import Importer


@Vows.batch
class Sha1GeneratorVows(Vows.Context):
    class ASha1Generator(Vows.Context):
        def topic(self):
            config = Config()
            importer = Importer(config)

            context = Context(None, config, importer)

            return BaseGenerator(context)

        class WhenNameIsPreserved(Vows.Context):
            def topic(self, generator):
                return generator.get('/unsafe/200x300/ignored_path/image.jpg')

            def should_ignore_path_prefix(self, topic):
                expect(topic).to_match('None/image.jpg')

        class WhenNameIsNotPreserved(Vows.Context):
            def topic(self, generator):
                return generator.get('/unsafe/200x300/ignored_path/image.jpg')

            def should_ignore_path_prefix(self, topic):
                expect(topic).to_match('None')

