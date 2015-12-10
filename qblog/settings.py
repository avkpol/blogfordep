"""
Django settings for qblog project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# import dj_database_url

# # Parse database configuration from $DATABASE_URL
# DATABASES = {'default': dj_database_url.parse('postgres://...')}
# HEROKU_POSTGRESQL_ONYX_URL = 'postgres://...'

# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# # Allow all host headers
# ALLOWED_HOSTS = ['*']

# # Enable Connection Pooling
# DATABASES['default']['ENGINE'] = 'django_postgrespool'
# PORT = 5432

# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# # Simplified static file serving.
# # https://warehouse.python.org/project/whitenoise/
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'







# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# email_info for gmail:
from email_info import *
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT

# default session storage "engines"

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_SAVE_EVERY_REQUEST = True



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mpjn+z)t_w0%nttcu$web9*@*br)^5qzgb@(gy$v%es23rs(%a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/'
# Application definition

INSTALLED_APPS = (
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    'social_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.angellist',
    'allauth.socialaccount.providers.bitbucket',
    'allauth.socialaccount.providers.bitly',
    'allauth.socialaccount.providers.coinbase',
    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.dropbox_oauth2',
    'allauth.socialaccount.providers.edmodo',
    'allauth.socialaccount.providers.evernote',
    # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.flickr',
    'allauth.socialaccount.providers.feedly',
    'allauth.socialaccount.providers.fxa',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.hubic',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.odnoklassniki',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.persona',
    'allauth.socialaccount.providers.soundcloud',
    'allauth.socialaccount.providers.spotify',
    'allauth.socialaccount.providers.stackexchange',
    'allauth.socialaccount.providers.tumblr',
    'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.vimeo',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.xing',
# my apps
    # 'ratings',
    'haystack',

    # 'secretballot',
    # 'likes',
    'blog',
    'checkout',
    'management',
    'django_markdown',
    
    # 'dajaxice',
    # 'dajax',


    
)
SOCIALACCOUNT_PROVIDERS = {
    'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}
        }

SOCIAL_AUTH_FACEBOOK_KEY = '1478893689105779'
SOCIAL_AUTH_FACEBOOK_SECRET = 'a91d4ac498612f176da70ad2fec6e314'

FACEBOOK_APP_ID='1478893689105779'
FACEBOOK_API_SECRET='a91d4ac498612f176da70ad2fec6e314'
FACEBOOK_APP_ACCESS_TOKEN='1478893689105779|PfHJrJ0VZ9lnjbjrlkU4VsQnOgY'
FACEBOOK_USER_ACCESS_TOKEN='CAAVBC8TZC7XMBAFqVZAADZB0geSgZBgmXIb07B2ATeHO98HtzgMCj9LBcZCpum6YlCxu8KasGVJGrE20AfOsUIsZCL4xYGFM7ZAYbpWr0vEgTlQWLQdTwIFfrCAxfuZAGCpFjRezeZBa57nFstzz2qINOCpj5aQm4Y9ieWh4ZAKXuVO0xRb1XNMUzldUVqqE6gs6nYZBMTwPFe0BAZDZD'

SITE_ID = 1
CRISPY_TEMPLATE_PACK = 'bootstrap3'

LOGIN_URL ='/accounts/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = "username_email" #(="username" | "email" | "username_email")
ACCOUNT_CONFIRM_EMAIL_ON_GET = True # (=False)
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL =  LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 10
ACCOUNT_EMAIL_REQUIRED = True 
ACCOUNT_EMAIL_VERIFICATION = None #choices are: "mandatory", "optional", or None
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Subject is: "
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http" #if secure use https
ACCOUNT_LOGOUT_ON_GET = False #log user out right away.
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL
ACCOUNT_SIGNUP_FORM_CLASS =None # add a custom sign up form
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION =True # use False if you don't want double password fields
ACCOUNT_UNIQUE_EMAIL= True #enforces emails are unique to all accounts
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username" # If you're using a Custom Model, maybe it's "email"
ACCOUNT_USER_MODEL_EMAIL_FIELD ="email" 
#ACCOUNT_USER_DISPLAY (=a callable returning user.username)
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_USERNAME_BLACKLIST =['some_username_youdon\'t_want']
ACCOUNT_USERNAME_REQUIRED =True #do you want them to have a user name?
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =False #don't show the password
ACCOUNT_PASSWORD_MIN_LENGTH =6 #min length of password
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =True #login the user after confirming email, if required.

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # custom middleware to collect http requests
    'management.custom_middleware.SaveRequestDb',
    # custom middleware for ajax messaging
    'management.ajax_messaging.AjaxMessaging',
    'likes.middleware.SecretBallotUserIpUseragentMiddleware',
)

ROOT_URLCONF = 'qblog.urls'

WSGI_APPLICATION = 'qblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"), )
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

TEMPLATE_CONTEXT_PROCESSORS = (

    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    #Django Generic Ratings
    "django.core.context_processors.request",
    
    # Required by `allauth` template tags
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    # Python social-auth
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
    

)




AUTHENTICATION_BACKENDS = (
   
    # for python social-auth
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    'social_auth.backends.facebook.FacebookBackend',
)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
        'TIMEOUT' : 60 
    },
}

# updates table everytime you add new record
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


