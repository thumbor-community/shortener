# -*- coding: utf-8 -*-

from thumbor.importer import Importer


class CommunityImporter(Importer):
    

    def __init__(self, config):
        '''
        :param config:
        '''
        super(CommunityImporter, self).__init__(config)

        self.shortener_backend = None
        self.shortener_generator = None

    def import_modules(self):

        super(CommunityImporter, self).import_modules()

        if self.config.SHORTENER_GENERATOR:
            self.import_item('SHORTENER_GENERATOR', 'Generator')

        if self.config.SHORTENER_STORAGE:
            self.import_item('SHORTENER_STORAGE', 'Storage')
