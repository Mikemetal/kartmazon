"""
Django settings for kartmazon project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ilwa=)%$18ttl0v70x!flw_u)3un6pc0=f*agj2e2()ew1b5*_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'ads',
    'ciudad',
    'estado',
    'follows',
    'fotosvehiculos',
    'marca',
    'modelo',
    'ofertas',
    'paquetes',
    'tipovehiculo',
    'usuariosperfil',
    'usuarios',
    'vehiculos',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'kartmazon.urls'

WSGI_APPLICATION = 'kartmazon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dd6fp3ujcr13fh',
        'HOST': 'ec2-54-204-43-138.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'mulucakwetqfxl',
        'PASSWORD': 'xBEDTlOmsgOhAAZE2CHAOSyQcV'
    }
    # 'desarrollo': {
    #     'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': 'kartmazon',                      # Or path to database file if using sqlite3.
    #     # The following settings are not used with sqlite3:
    #     'USER': 'root',
    #     'PASSWORD': 'w4p1ll0',
    #     'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
    #     'PORT': '',                      # Set to empty string for default.
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': 'kartmazon',                      # Or path to database file if using sqlite3.
    #     # The following settings are not used with sqlite3:
    #     'USER': 'root',
    #     'PASSWORD': 'w4p1ll0',
    #     'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
    #     'PORT': '',                      # Set to empty string for default.
    # }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Tijuana'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # 'PAGINATE_BY': 50,                 # Default to 10
    # 'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    # 'MAX_PAGINATE_BY': 100,             # Maximum limit allowed when using `?page_size=xxx`.
 # 'DEFAULT_PERMISSION_CLASSES': (
 #     'rest_framework.permissions.IsAdminUser','rest_framework.permissions.IsAuthenticated'
 # ),
 'DEFAULT_PARSER_CLASSES': (
     'rest_framework.parsers.FileUploadParser',
 ),
 'DEFAULT_AUTHENTICATION_CLASSES': (
     'rest_framework.authentication.TokenAuthentication',
     'rest_framework.authentication.SessionAuthentication',
 ),
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
if os.environ.get('HEROKU'):  # heroku config:set HEROKU=1
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MAX_UPLOAD_SIZE = 20971520  # 20MB
CONTENT_TYPES = ['application/pdf', 'image/jpeg', 'image/png']  # .pdf, .jpeg and .png

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

CORS_ORIGIN_ALLOW_ALL = True