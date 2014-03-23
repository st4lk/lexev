""""""
import os

DEBUG = False


TIME_ZONE = 'UTC'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['OPENSHIFT_APP_NAME'],
        'USER': os.environ['OPENSHIFT_DB_USERNAME'],
        'PASSWORD': os.environ['OPENSHIFT_DB_PASSWORD'],
        'HOST': os.environ['OPENSHIFT_DB_HOST'],
        'PORT': os.environ['OPENSHIFT_DB_PORT'],
    }
}

os.environ['PYTHON_EGG_CACHE'] = '/tmp'
MEDIA_ROOT = os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'media')

LINKEDIN_CONSUMER_KEY = os.environ['LINKEDIN_CONSUMER_KEY']
LINKEDIN_CONSUMER_SECRET = os.environ['LINKEDIN_CONSUMER_SECRET']
LINKEDIN_USER_TOKEN = os.environ['LINKEDIN_USER_TOKEN']
LINKEDIN_USER_SECRET = os.environ['LINKEDIN_USER_SECRET']
LINKEDIN_RETURN_URL = os.environ['LINKEDIN_RETURN_URL']
if 'true' in os.environ['LINKEDIN_STORE_CACHE'].lower():
    LINKEDIN_STORE_CACHE = True
else:
    LINKEDIN_STORE_CACHE = False
