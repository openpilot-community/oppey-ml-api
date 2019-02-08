# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dotenv
import dj_database_url
import django_heroku
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fsch+6!=q+@ol&%0x!nwdl@48^ixbd4clx5f1i!5n^66y+pmn*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inspectdb_refactor',
    'chatterbot.ext.django_chatterbot',
    'oppey_ml_api',
)

# OppeyML settings

CHATTERBOT = {
    'name': 'Oppey ML',
    'preprocessors': [
        'chatterbot.preprocessors.clean_whitespace'
    ],
    'logic_adapters': [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    'filters': [
      'filters.get_recent_repeated_responses'
    ]
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
)
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
ROOT_URLCONF = 'oppey_ml_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oppey_ml_api.wsgi.application'

django_heroku.settings(locals())
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {}
# print("db_url: {0}".format(os.environ.get("DATABASE_URL")))
# db_settings = dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=600)
# print("db_settings: {0}".format(db_settings))
# DATABASES['default'] = db_settings
locals()['DATABASES']['default'] = dj_database_url.config(conn_max_age=django_heroku.MAX_CONN_AGE)
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
  os.path.join(
    os.path.dirname(__file__),
    'static',
  ),
)