import os
from .common import *
import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = []
CORS_ALLOWED_ORIGINS = []

DATABASES = {
  'default': dj_database_url.config()
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    
RENDER_EXTERNAL_CORS_ORIGINS = os.environ.get('RENDER_EXTERNAL_CORS_ORIGINS')
if RENDER_EXTERNAL_CORS_ORIGINS:
    origins = RENDER_EXTERNAL_CORS_ORIGINS.split(',')
    CORS_ALLOWED_ORIGINS += origins
    print('CORS_ALLOWED_ORIGINS are : ', CORS_ALLOWED_ORIGINS)
    