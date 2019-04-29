"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@!-)jwmuzh8btr380g61=g+#&zzei&dz2(&=xbvxztady)_p(r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'makori.django.projects@gmail.com'
EMAIL_HOST_PASSWORD = 'j112o358B@#$%^&*'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = 'Moi Market Place <makori.django.projects@gmail.com>'
BASE_URL = 'https://www.moimarketplace.com'


MANAGERS = (
    ('Job makori', "makori.django.projects@gmail.com"),
    ('Sam Emekui',''),
    ('Ramadhan', ''),
    ('Gedion','langatbmt@gmail.com'),
)

ADMINS = MANAGERS



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party
    'stripe',
    'storages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'django_extensions',
    #For PayPall
    'paypal.standard.ipn',

    #our apps
    'accounts',
    'addresses',
    'analytics',
    'billing',
    'carts',
    'marketing',
    'orders',
    'products',
    'search',
    'tags',
    'widget_tweaks',
    'crispy_forms',
    'payment',
]

SITE_ID  = 1 
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

AUTH_USER_MODEL = 'accounts.User' #changes the built-in user model to ours
LOGIN_URL = '/login/'
LOGIN_URL_REDIRECT = '/'
LOGOUT_URL = '/logout/'

FORCE_SESSION_TO_ONE = False
FORCE_INACTIVE_USER_ENDSESSION= False



MAILCHIMP_API_KEY       = "717d0854ed20fed3be3689a3f125915c-us17"
MAILCHIMP_DATA_CENTER   = "us17"
MAILCHIMP_EMAIL_LIST_ID = "e2ef12efee"

#Sripe Payment api
STRIPE_SECRET_KEY = 'sk_test_9L5gZM2ye23FYOYwc8VIdV08'
STRIPE_PUB_KEY    = 'pk_test_4h7bslHSkigi9dPKb4fmxFon'

#paypal payment API
PAYPAL_RECEIVER_EMAIL='makori.django.projects@gmail.com'
PAYPAL_TEST = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.PersistentRemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

LOGOUT_REDIRECT_URL = '/login/'
ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.csrf',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'com311',
        'USER':'reflex',
        'PASSWORD':'reflex',
        'HOST':'',
        'PORT':'',
        'ATOMIC_REQUESTS': True,
        'AUTOCOMMIT': True,
        'CONN_MAX_AGE': 60,
        'TIME_ZONE': 'Africa/Nairobi',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'sw'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
PROTECTED_ROOT = os.path.join(BASE_DIR, "static", "protected_media")
MEDIA_ROOT = os.path.join(BASE_DIR,'static', 'media')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static', 'static_files'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')



CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

# Add the 'allauth' backend to AUTHENTICATION_BACKEND and keep default ModelBackend
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
						   'django.contrib.auth.backends.RemoteUserBackend',
                           'allauth.account.auth_backends.AuthenticationBackend']
# EMAIL_BACKEND so allauth can proceed to send confirmation emails
# ONLY for development/testing use console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Custom allauth settings
# Use email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = ['email', ]
ACCOUNT_EMAIL_REQUIRED = True
# Make email verification mandatory to avoid junk email accounts
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# Eliminate need to provide username, as it's a very old practice
ACCOUNT_USERNAME_REQUIRED = False
