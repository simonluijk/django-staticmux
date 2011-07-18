#!/usr/bin/env python
#-*- coding:utf-8 -*-

from distutils.core import setup

setup(
    name = 'staticmux',
    description = 'Django app to simplifiy development and deployment of CSS and Javascript for Django projects.',
    version = '0.0.1',
    author = 'Simon Luijk',
    author_email = 'simon@luijk.co.uk',
    url = 'http://www.apricotwebsolutions.com/',
    packages = [
        'staticmux',
        'staticmux.conf',
        'staticmux.filters',
        'staticmux.management',
        'staticmux.management.commands',
        'staticmux.templatetags',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Utilities'
    ],
)
