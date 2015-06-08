# -*- coding: utf-8 -*-


from .context import CommunityExtensions


CommunityExtensions.register_module(
    config_key='SHORTENER_STORAGE',
    class_name='Storage',
    multiple=False
)
