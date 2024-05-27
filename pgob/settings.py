import os
from datetime import timedelta
from pathlib import Path

import environ
from corsheaders.defaults import default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, True),
    USE_SQLITE=(bool, False),
)

env_file = os.path.join(BASE_DIR, '.env')

if os.path.isfile(env_file):
    env.read_env(env_file)
else:
    raise Exception('No local .env detected.')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_spectacular',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters',
    'import_export',

    'accreditations.apps.AccreditationsConfig',
    'core.apps.CoreConfig',
    'national_accreditation.apps.NationalAccreditationConfig',
    'overflight_non_commercial_aircraft.apps.OverflightNonCommercialAircraftConfig',
    'international_accreditation.apps.InternationalAccreditationConfig',
    'security_accreditations.apps.SecurityAccreditationsConfig',
    'equipments.apps.EquipmentsConfig',
    'vehicles.apps.VehiclesConfig',
    'vehicle_access_airport_accreditations.apps.VehicleAccessAirportAccreditationsConfig',
    'intercom_equipment_declaration.apps.IntercomEquipmentDeclarationConfig',
    'general_vehicle_accreditation.apps.GeneralVehicleAccreditationConfig',
    'profiles.apps.ProfilesConfig',
    'media_channels.apps.MediaChannelsConfig',
    'countries.apps.CountriesConfig',
    'positions.apps.PositionsConfig',
    'pgob_auth.apps.PgobAuthConfig',
    'allergies.apps.AllergiesConfig',
    'immunizations.apps.ImmunizationsConfig',
    'medical_histories.apps.MedicalHistoriesConfig',
    'notifications.apps.NotificationsConfig',
    'credentials.apps.CredentialsConfig',
    'housing.apps.HousingConfig',
    'commerce.apps.CommerceConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djangorestframework_camel_case.middleware.CamelCaseMiddleWare',
]

ROOT_URLCONF = 'pgob.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'pgob.wsgi.application'

# Django Rest Framework Settings
# https://www.django-rest-framework.org/
# https://github.com/vbabiy/djangorestframework-camel-case
# https://dj-rest-auth.readthedocs.io/en/latest/

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=20),
}

# Swagger settings
# https://github.com/tfranzel/drf-spectacular

SPECTACULAR_SETTINGS = {
    'TITLE': 'PGOB API',
    'DESCRIPTION': 'The official PGOB API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'CAMELIZE_NAMES': True,
    'POSTPROCESSING_HOOKS': [
        'drf_spectacular.hooks.postprocess_schema_enums',
        'drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields',
    ],
    'ENUM_NAME_OVERRIDES': {

    }
}

# CORS Configuration
# https://pypi.org/project/django-cors-headers/

# API_KEY_CUSTOM_HEADER = 'HTTP_X_API_KEY'

# CORS_ALLOWED_ORIGINS = ['*']

CORS_ALLOW_HEADERS = [
    *default_headers,
    # 'X-Api-Key',
    # 'Authorization',
]

CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if env('USE_SQLITE'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            'PORT': env('DB_PORT'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

USE_I18N = True
USE_TZ = True
TIME_ZONE = 'America/Panama'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'pgob', 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALLOWED_HOSTS = ['*']

LOGIN_URL = 'auth:login'
LOGIN_REDIRECT_URL = 'auth:index'
LOGOUT_REDIRECT_URL = 'auth:index'

# Email settings

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fizzbazz.labs@gmail.com'
EMAIL_HOST_PASSWORD = 'okqzitaawmjnuexy'
DEFAULT_FROM_EMAIL = 'fizzbazz.labs.@gmail.com'

# App Envs
APP_HOST = env('APP_HOST')
FRONTEND_DETAIL_URL = env('FRONTEND_DETAIL_URL')

# PowerBI Settings
POWERBI_CLIENT_ID = env('POWERBI_CLIENT_ID')
POWERBI_TENANT_ID = env('POWERBI_TENANT_ID')
POWERBI_CLIENT_SECRET = env('POWERBI_CLIENT_SECRET')
