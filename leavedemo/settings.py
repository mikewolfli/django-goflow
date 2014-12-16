# Django settings for openflow project.
from os.path import dirname, join 
_dir = dirname(__file__)

LIB_PATH = join(_dir,'..')
import sys
sys.path.append(LIB_PATH)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

LOGIN_URL = 'accounts/login/'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

#DATABASE_ENGINE = 'sqlite3'           # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
#DATABASE_NAME = join(_dir, 'sqlite.db3')             # Or path to database file if using sqlite3.
#DATABASE_USER = ''             # Not used with sqlite3.
#DATABASE_PASSWORD = ''         # Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
WSGI_APPLICATION = 'wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(_dir, 'db.sqlite3'),
    }
}

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
#TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

ROOT_URL = '/'
MEDIA_ROOT = join(_dir, 'media/files/')
LOGIN_URL = ROOT_URL +'login/'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = MEDIA_URL +'admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%@48o#l@iz!ybjl_2_1smc#%*u+^m0m^18ghw-6=3k48g2rt8^'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'goflow.workflow',
    'goflow.graphics2',
    'goflow.runtime',
    'goflow.apptools',
    'leavedemo.leave',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.load_template_source',
)

ROOT_URLCONF = 'leavedemo.urls'

TEMPLATE_DIRS = (
    join(_dir,'..', 'goflow', 'apptools', 'templates').replace('\\','/'),
    join(_dir,'..', 'goflow', 'runtime', 'templates').replace('\\','/'),
    join(_dir,'..', 'goflow', 'workflow', 'templates').replace('\\','/'),
)

# user profile model
#AUTH_PROFILE_MODULE = 'workflow.userprofile'

TEST_USERS = (
            ('primus','p'),('notarius','n'),('prefectus','p'),
            ('socius','s'),('secundus','s'),('tertius','t'),('quartus','q')
)
WF_USER_AUTO = 'auto'
WF_APPS_PREFIX = '/leave'
WF_PUSH_APPS_PREFIX = 'leavedemo.leave.pushapplications'

# mail notification settings
DEFAULT_FROM_EMAIL = 'goflow <goflow@alwaysdata.net>'
EMAIL_HOST = 'smtp.alwaysdata.com'
EMAIL_SUBJECT_PREFIX = '[Goflow notification]'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT= join(_dir,'static/files/')
STATIC_URL= '/static/'