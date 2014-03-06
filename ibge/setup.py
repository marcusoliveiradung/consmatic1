#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2011 Guilherme Gondim
# Copyright (c) 2009 Interlegis
#
# This file is part of Django IBGE.
#
#   Django IBGE is free software under terms of the GNU General Public License
#   version 3 (GPLv3) as published by the Free Software Foundation.  See the
#   file README for copying conditions.
#

from distutils.core import setup

setup(
    name = 'ibge',
    version = '0.1.2',
    description = 'Django IBGE application',
    long_description = ('Django application to provide information from '
                        'Brazilian Institute of Geography and Statistics '
                        '(IBGE).'),
    keywords = 'django apps ibge',
    author = 'Guilherme Gondim',
    author_email = 'semente@taurinus.org',
    url = 'https://bitbucket.org/semente/django-ibge',
    download_url = 'https://bitbucket.org/semente/django-ibge/downloads',
    license = 'GNU General Public License (GPL), Version 3',
    classifiers = [
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = ['ibge'],
    package_dir={'ibge': 'ibge'},
    package_data={'ibge': ['fixtures/*.json']},
)
