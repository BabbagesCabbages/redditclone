#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import redditclone
version = redditclone.__version__

setup(
    name='redditclone',
    version=version,
    author="karson",
    author_email='karsonmadden@gmail.com',
    packages=[
        'redditclone',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['redditclone/manage.py'],
)
