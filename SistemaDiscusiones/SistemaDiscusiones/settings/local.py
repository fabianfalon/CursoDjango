from .base import * 

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER': 'cursodjango',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT' : '5432',
    }
}


STATIC_URL = '/static/'
