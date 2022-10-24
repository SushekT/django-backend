from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Your Secret KEY'

INSTALLED_APPS += (
    'debug_toolbar',
    'drf_yasg',
    'django_extensions'
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ['127.0.0.1', ]

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

# Email Configuration

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'your_user_id'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = '2525'
