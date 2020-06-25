#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Maria Jose'
SITENAME = 'Machine Learning Astronauta'
SITEURL = "https://c3rssei.github.io/Blog"
SITESUBTITLE = "Un viaje por la galaxia del data science"
DESCRIPTION = "Bitacora personal sobre data science y machine learning"
FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/vnd.microsoft.icon'

META_IMAGE = SITEURL + "/static/img/og_logo.jpg"
META_IMAGE_TYPE = "image/jpeg"

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
SOCIAL = (('twitter', 'https://twitter.com/luca_chr'),
    ('google-plus-square', 'https://plus.google.com/117284397605208270870'),
    ('github', 'https://github.com/lucachr'),
    ('envelope', 'mailto:luca92web@gmail.com'),)

DEFAULT_PAGINATION = 5
THEME = "pelican-themes/mg"
#BOOTSTRAP_THEME = 'flatly'

DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'
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
RELATIVE_URLS = False
DISPLAY_PAGES_ON_MENU=True
