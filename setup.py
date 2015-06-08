# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='thumbor_community.shortener',
    version='0.1',
    url='http://github.com/thumbor_community/shortener',
    license='MIT',
    author='Thumbor Community',
    description='URL Shortener',
    packages=['thumbor_community.shortener'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'thumbor',
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
