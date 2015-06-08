# -*- coding: utf-8 -*-

from thumbor.context.Context import Context, ContextImporter
from thumbor_shortener.importer import CommunityImporter


class CommunityExtensions(object):

    @classmethod
    def register_module(cls, config, klass, multiple=False):
        CommunityContextImporter.register(config.lower())
        CommunityImporter.register(config, klass, multiple)


class CommunityContextImporter(ContextImporter):

    __community_modules = []

    @classmethod
    def register(cls, name):
        cls.__community_modules.append(name)

    def __init__(self, context, importer):
        '''
        :param context:
        :param importer:
        '''

        super(CommunityContextImporter, self).__init__(self, context, importer)

        # Dynamically load registered modules
        for name in self.__community_modules:
            if getattr(importer, name):
                instance = getattr(importer, name)(context)
                setattr(self, name, instance)
            else:
                setattr(self, name, None)


class CommunityContext(Context):

    def __init__(self, server=None, config=None, importer=None,
                 request_handler=None):
        '''
        Class responsible for containing:
        * Server Configuration Parameters (port, ip, key, etc);
        * Configurations read from config file (or defaults);
        * Importer with imported modules (engine, filters, detectors, etc);
        * Request Parameters (width, height, smart, meta, etc).

        Each instance of this class MUST be unique per request.
        This class should not be cached in the server.

        :param server:
        :param config:
        :param importer:
        :param request_handler:
        '''

        super(CommunityContext, self).__init__(
            server=server,
            config=config,
            importer=None,  # Always load our ContextImporter
            request_handler=request_handler
        )

        # Load our ContextImporter
        if importer:
            self.modules = CommunityContextImporter(self, importer)
