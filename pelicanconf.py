#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jonathan Branam'
SITENAME = 'Jonathan Branam'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Indiana/Indianapolis'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

PLUGIN_PATHS = ['../pelican-plugins']

PLUGINS = [
        'assets',
]

THEME = '../taman'
# THEME = '../pelican-themes/taman'

# taman theme
USER_LOGO_URL = '/images/JPB_headshot.jpg'
TAGLINE = '''
Data Scientist and Engineer
'''
# end taman theme

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         )

# Social widget
SOCIAL = (('twitter', 'JonathanBranam'),
          ('linkedin', 'JonathanBranam'),
          ('github', 'jonathanbranam'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
