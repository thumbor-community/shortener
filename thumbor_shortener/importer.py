# -*- coding: utf-8 -*-

from thumbor.importer import Importer


class CommunityImporter(Importer):

    __community_modules = []

    @classmethod
    def register_module(cls, config_key, class_name, multiple=False):
        cls.__community_modules.append(dict(
            config_key=config_key,
            class_name=class_name,
            multiple=multiple
        ))

    def __init__(self, config):
        '''
        :param config:
        '''
        super(CommunityImporter, self).__init__(config)

        # Autoload
        for module in self.__community_modules:
            setattr(self, module.config_key.lower(), None)

    def import_modules(self):
        super(CommunityImporter, self).import_modules()

        # Autoload
        for module in self.__community_modules:
            if hasattr(self.config, module.config_key):
                self.import_item(module.config_key, module.class_name)
