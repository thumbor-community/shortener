# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='tc_shortener',
    version='0.2',
    url='http://github.com/thumbor-community/shortener',
    license='MIT',
    author='Thumbor Community',
    description='URL Shortener',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'thumbor',
        'tc_core',
        'shortuuid'
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
