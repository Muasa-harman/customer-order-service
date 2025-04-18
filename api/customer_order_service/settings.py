"""
Django settings for customer_order_service project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/

"""
from datetime import timedelta
from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^2867@su1w%zt39kla1i$zd33+m$zz_wh%)s(g-b=djv8^3!@c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
from dotenv import load_dotenv
load_dotenv()


env = environ.Env()
environ.Env.read_env()

AUTHENTICATION_BACKENDS = [
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend', 
    'django.contrib.auth.backends.ModelBackend',
    # update
    'graphql_jwt.backends.JSONWebTokenBackend',
    # 'users.backends.OIDCAuthenticationBackend',
    # 'oidc_auth.auth.OIDCAuthenticationBackend',
]

OIDC_ENDPOINT = "http://localhost:8080/realms/master/broker/keycloak-oidc/endpoint" 
OIDC_CLIENT_ID = os.getenv('OIDC_CLIENT_ID')
OIDC_CLIENT_SECRET = os.getenv('OIDC_CLIENT_SECRET')

AUTH_USER_MODEL = 'auth.CustomUser'

GRAPHQL_JWT = {
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=6),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_HAS_REFRESH_EXP_HANDLER': True,
    'JWT_PAYLOAD_HANDLER': 'auth.utils.jwt_payload_handler',
}

OIDC_ISSUER = os.getenv('OIDC_ISSUER')

OIDC_OP_AUTHORIZATION_ENDPOINT = f"{OIDC_ISSUER}/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = f"{OIDC_ISSUER}/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = f"{OIDC_ISSUER}/protocol/openid-connect/userinfo"
OIDC_OP_LOGOUT_ENDPOINT = f"{OIDC_ISSUER}/protocol/openid-connect/logout"
OIDC_OP_JWKS_ENDPOINT = f"{OIDC_ISSUER}/protocol/openid-connect/certs"

OIDC_RP_CLIENT_ID = os.getenv('OIDC_CLIENT_ID')
OIDC_RP_CLIENT_SECRET = os.getenv('OIDC_CLIENT_SECRET')

AUTH_USER_MODEL = 'users.CustomUser'

OIDC_ADMIN_ROLE = 'admin'

# Django Settings
LOGIN_URL = 'oidc_authentication_init'
LOGOUT_REDIRECT_URL = '/admin/'
LOGIN_REDIRECT_URL = '/admin/'



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'graphene_django',
    'users.apps.UsersConfig',
    'customers',
    'orders',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mozilla_django_oidc.middleware.SessionRefresh',
]

ROOT_URLCONF = 'customer_order_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'customer_order_service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'), 
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST', default='localhost'),
        'PORT': env('POSTGRES_PORT', default='5432'),
    }
}
# GraphQL 
GRAPHENE = {
    'SCHEMA': 'customer-order-service.schema.schema',
     'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

AUTHENTICATION_CLASSES = [
    'oidc_auth.authentication.JSONWebTokenAuthentication',
]

AUTH_USER_MODEL = 'users.CustomUser' 
# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
