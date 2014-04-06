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
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '1469027933326416'
SOCIAL_AUTH_FACEBOOK_SECRET = 'd6355052e2f80d98a315b9aa5b5cf851'

SOCIAL_AUTH_TWITTER_KEY = 'ODrnV90JplKRpKE4WNVRZIe1L'
SOCIAL_AUTH_TWITTER_SECRET = 'LG31AIFJ4GQsAcfsC8gcatwUeOtlfg6SnxXhHcYpsqJrSAzy2a'

MANDRILL_API_KEY = 'B7lPKBe39KmpXQTjtJF68g'
