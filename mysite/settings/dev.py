from .common import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'll@rrh1@%evim04w&1xrs6if@5z^qg%jn5!(hbz_kvj-pgi$cj'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','.loca.lt']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoAssgn_db',
        'HOST': 'localhost',
        'USER': 'djangoAssgn_app',
        'PASSWORD': '1234'
    }
}
