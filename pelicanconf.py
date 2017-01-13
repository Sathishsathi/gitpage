#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sathish Kumar'
SITENAME = u'. > Sathish Kumar K'
SITEURL = ''
SITELOGO = '../images/profile.png'
SITEDESCRIPTION = 'Thoughts and Writings'
SITETITLE = AUTHOR
PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

THEME = "pelican-flex"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS =  (
         ('Activities','../category/post.html'),
         ('Technical','../category/technical.html'),
	 ('Python','/category/python.html'),
         ('View all','../archives.html'),
         ('About me', '../authors.html'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/sathish.kokila.9'),
          ('gitlab', '#'),('github','https://github.com/Sathishsathi'))

DEFAULT_PAGINATION = 8

# Static files
STATIC_PATHS = ['images', 'pdfs']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
