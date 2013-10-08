""""""
import os

DEBUG = False

# BROKER_URL = os.environ['OPENSHIFT_NOSQL_DB_URL']

TIME_ZONE = 'UTC'

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.mysql',
        'NAME'      : os.environ['OPENSHIFT_APP_NAME'],
        'USER'      : os.environ['OPENSHIFT_DB_USERNAME'],
        'PASSWORD'  : os.environ['OPENSHIFT_DB_PASSWORD'],
        'HOST'      : os.environ['OPENSHIFT_DB_HOST'],
        'PORT'      : os.environ['OPENSHIFT_DB_PORT'],
    }
}

os.environ['PYTHON_EGG_CACHE'] = '/tmp'
MEDIA_ROOT = join(os.environ.get('OPENSHIFT_DATA_DIR'), 'media')
