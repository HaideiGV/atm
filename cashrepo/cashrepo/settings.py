"""
Django settings for cashrepo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# import djcelery
# djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#g-!#i6mbd8sn8txj%ai!6bch-o@pp9vztk**n^zgvj1ljpf)o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
INTERNAL_IPS = ['127.0.0.1',  '::1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cash',
    'debug_toolbar',
)

# INSTALLED_APPS += ("djcelery", )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'cashrepo.urls'

WSGI_APPLICATION = 'cashrepo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dfo8c49bgbngej',
#         'USER': 'qbdaiyocrryhqo',
#         'PASSWORD': 'yLLnHr3up_Ab-6MzpEBvWdK26M',
#         'HOST': 'ec2-54-83-199-54.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = False

DEBUG_TOOLBAR_PATCH_SETTINGS = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/static/'
# if DEBUG:
#     MEDIA_URL = '/media/'
#     STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
#     MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'media')
#     STATICFILES_DIRS = (
#         os.path.join(os.path.dirname(BASE_DIR), 'static', 'static'),
#     )


TEMPLATE_DIR = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


