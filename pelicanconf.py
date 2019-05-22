#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nik Davis'
SITENAME = "Nik Davis"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
# ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

ARTICLE_URL = 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'

# YEAR_ARCHIVE_URL = 'posts/{date:%Y}/'
YEAR_ACHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Activate ipynb plugin
# MARKUP = ('md', 'ipynb')
# PLUGIN_PATHS = ['./plugins']
# PLUGINS = ['ipynb.markup']

# Activate liquid tags plugin
MARKUP = ('md', )

PLUGIN_PATHS = ['plugins', 'plugins/pelican-plugins']
PLUGINS = ['ipynb.liquid']

IGNORE_FILES = ['.ipynb_checkpoints']

# Theme settings
THEME = 'theme'

ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'nikdavis0'
GITHUB_USERNAME = 'nik-davis'
STACKOVERFLOW_ADDRESS = 'https://stackoverflow.com/users/10202890/nik-davis'
SHOW_ARCHIVES = True

STATIC_PATHS = ['images', 'notebooks', 'favicon.ico']
