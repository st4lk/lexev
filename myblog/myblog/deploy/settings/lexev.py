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


def get_bool_env_value(env_name):
    if 'true' in os.environ[env_name].lower():
        return True
    else:
        return False


LINKEDIN_CONSUMER_KEY = os.environ['LINKEDIN_CONSUMER_KEY']
LINKEDIN_CONSUMER_SECRET = os.environ['LINKEDIN_CONSUMER_SECRET']
LINKEDIN_USER_TOKEN = os.environ['LINKEDIN_USER_TOKEN']
LINKEDIN_USER_SECRET = os.environ['LINKEDIN_USER_SECRET']
LINKEDIN_RETURN_URL = os.environ['LINKEDIN_RETURN_URL']
LINKEDIN_STORE_CACHE = get_bool_env_value('LINKEDIN_STORE_CACHE')

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = int(os.environ['EMAIL_PORT'])
EMAIL_USE_TLS = get_bool_env_value('EMAIL_USE_TLS')
