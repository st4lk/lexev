# -*- coding: utf-8 -*-
# Django settings for myblog project.

import sys
import warnings
import os
from os.path import dirname
from django.utils.importlib import import_module

DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_DIR = dirname(os.path.abspath(__file__))

ADMINS = (
    ('stalk', 'alexevseev@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'data.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'locale'),
)


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, "public", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, "public", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, "static"),
    # 'd:/Dropbox/Development/Django/django14_study/myblog/myblog/static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
# Fill it manually or assign from env variable
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'myblog.utils.middleware.RuRedirectMiddleware',
    'solid_i18n.middleware.SolidLocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",

    "myblog.utils.context_processors.DjangoVersionContextProcessor",
    "myblog.utils.context_processors.PythonVersionContextProcessor",
    "myblog.utils.context_processors.DisqusContextProcessor",
    "myblog.utils.context_processors.FeedBurnerContextProcessor",
)

ROOT_URLCONF = 'myblog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'myblog.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'django.contrib.markup',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.sitemaps',

    'haystack',
    "south",
    "articles",

    'pages',
    'myblog.utils',
    'cv',
    'articles_custom'
)

ARTICLES_AUTO_TAG = False

ARTICLES_TEASER_LIMIT = 75

FEEDBURNER_URL = 'http://feeds.feedburner.com/{lang}_lexevorg'
# cache feed for this amount of seconds
ARTICLE_FEED_TIMEOUT = 3600

#TRANSMETA settings
TRANSMETA_DEFAULT_LANGUAGE = 'en'

# Change this to be your Disqus site's short name
DISQUS_FORUM_SHORTNAME = 'lexev-dev'

OPENSHIFT_GEAR_NAME = os.environ.get('OPENSHIFT_GEAR_NAME', None)

# Put your Disqus API key here (only necessary if you're porting comments from django.contrib.comments)
# DISQUS_USER_API_KEY = 'short_name'

# Configure articles from email
# ARTICLES_FROM_EMAIL = {
#     'protocol': 'IMAP4',
#     'host': 'mail.yourserver.com',
#     'port': 9000,
#     'keyfile': '/path/to/keyfile',
#     'certfile': '/path/to/certfile',
#     'user': 'your_username',
#     'password': 'your_password',
#     'ssl': True,
#     'autopost': True,
#     'markup': 'r',
#     'acknowledge': True,
# }


MARKDOWN_EXTENSIONS = (
    'markdown.extensions.tables',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_DIR, 'whoosh_index'),
    },
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
if OPENSHIFT_GEAR_NAME is None:
    LOGS_DIR = os.path.join(dirname(PROJECT_DIR), "logs")
else:
    LOGS_DIR = os.environ['OPENSHIFT_LOG_DIR']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'myblog.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'rotating_file': {
            'level':       'DEBUG',
            'formatter':   'main_formatter',  # from the django doc example
            'class':       'logging.handlers.RotatingFileHandler',
            'filename':    os.path.join(LOGS_DIR, "django.log"),
            'maxBytes':    1024*1024*1,  # 1 MB
            'backupCount': 7,
        },
        'linkedin_file': {
            'level':       'DEBUG',
            'formatter':   'main_formatter',  # from the django doc example
            'class':       'logging.handlers.RotatingFileHandler',
            'filename':    os.path.join(LOGS_DIR, "linkedin.log"),
            'maxBytes':    1024*1024*1,  # 1 MB
            'backupCount': 7,
        },
        'db_file': {
            'level':       'INFO',
            'filters': ['require_debug_true'],
            'formatter':   'main_formatter',  # from the django doc example
            'class':       'logging.handlers.RotatingFileHandler',
            'filename':    os.path.join(LOGS_DIR, "db.log"),
            'maxBytes':    1024*1024*1,  # 1 MB
            'backupCount': 7,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        "": {
            'handlers': ['rotating_file', 'console'],
            'level': 'INFO',
        },
        "linkedin": {
            'handlers': ['linkedin_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        "django.db": {
            'handlers': ['db_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}

ALLOWED_HOSTS = ["*"]

# Linked-in settings
# Keys can be obtained here:
# https://www.linkedin.com/secure/developer
LINKEDIN_CONSUMER_KEY = "TBD"
LINKEDIN_CONSUMER_SECRET = "TBD"
LINKEDIN_USER_TOKEN = "TBD"
LINKEDIN_USER_SECRET = "TBD"
LINKEDIN_RETURN_URL = "TBD"
LINKEDIN_STORE_CACHE = "TBD"

# EMAIL settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "TBD"
EMAIL_HOST_USER = "TBD"
EMAIL_HOST_PASSWORD = "TBD"
EMAIL_PORT = "TBD"
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

try:
    from settings_local import *
except ImportError:
    pass


def override_settings(dottedpath):
    """Imports uppercase modules from an string based module.
    Example:
        override_settings('my.module.settings')
    """
    try:
        _m = import_module(dottedpath)
    except ImportError:
        warnings.warn("Failed to import %s" % dottedpath)  # <-- will show up in your error log
    else:
        _thismodule = sys.modules[__name__]
        for _k in dir(_m):  # <-- moved the block inside else
            if _k.isupper() and not _k.startswith('__'):
                setattr(_thismodule, _k, getattr(_m, _k))

# Import openshift settings
if OPENSHIFT_GEAR_NAME is not None:
    override_settings('myblog.deploy.settings.' + OPENSHIFT_GEAR_NAME)
