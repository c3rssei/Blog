#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Maria Jose'
SITENAME = 'Machine Learning Astronauta'
SITEURL = 'https://c3rssei.github.io/'

PATH = '/home/mariajose/Blog2/content'
DEFAULT_LANG = 'en'
TIMEZONE = 'UTC'


DEFAULT_DATE_FORMAT = '%B %d, %Y'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5
THEME = "pelican-themes/mg"
BOOTSTRAP_THEME = 'flatly'
TYPOGRIFY = True
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
STATIC_PATHS = ["theme/images",'images']
PLUGIN_PATHS = ['/home/mariajose/Blog2/pelican-plugins']
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'render_math',
    'pelican-ipynb.markup',
"tipue_search",
]
I18N_TEMPLATES_LANG = 'en'
IPYNB_USE_METACELL = True

MARKUP = ('md', 'ipynb')

IGNORE_FILES = [".ipynb_checkpoints"]  
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU=True