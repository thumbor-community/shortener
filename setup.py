# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='tc_shortener',
    version='0.1',
    url='http://github.com/thumbor-community/shortener',
    license='MIT',
    author='Thumbor Community',
    description='URL Shortener',
    packages=['tc_shortener'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'thumbor',
        'tc_core'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
