# -*- coding: utf-8 -*-


from thumbor_community import CommunityExtensions


CommunityExtensions.register_module(
    config_key='SHORTENER_STORAGE',
    class_name='Storage',
    multiple=False
)
