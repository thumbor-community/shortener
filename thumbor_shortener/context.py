# -*- coding: utf-8 -*-

from thumbor.context.Context import Context, ContextImporter


class CommunityContextImporter(ContextImporter):

    def __init__(self, context, importer):
        '''
        :param context:
        :param importer:
        '''

        super(CommunityContextImporter, self).__init__(self, context, importer)

        self.shortener_storage = None
        if importer.shortener_storage:
            self.shortener_storage = self.shortener_storage(context)

        self.shortener_generator = None
        if importer.shortener_generator:
            self.shortener_generator = self.shortener_generator(context)


class CommunityContext(Context):

    def __init__(self, server=None, config=None, importer=None, request_handler=None):
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
            importer=None, # Always load our ContextImporter
            request_handler=request_handler
        )

        # Load our ContextImporter
        if importer:
            self.modules = CommunityContextImporter(self, importer)


