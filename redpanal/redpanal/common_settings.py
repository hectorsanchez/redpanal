# Django settings for redpanal project.
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

SITE_ID = 1

LANGUAGES = (
    ('es', 'Spanish'),
    ('en', 'English'),
    ('pt', 'Portuguese'),
)

LANGUAGE_CODE = 'es'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    "redpanal.utils.context_processors.git_hash"
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = 'redpanal.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'redpanal.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'haystack',
    'redpanal.audio',
    'redpanal.project',
    'redpanal.core',
    'redpanal.social',
    'redpanal.users',
    'redpanal.utils',
    'taggit',
    'crispy_forms',
    'south',
    'actstream',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'avatar',
    'endless_pagination',
    'easy_thumbnails',
)


ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda o: "/u/%s/" % o.username,
}

ACTSTREAM_SETTINGS = {
    'MANAGER': 'actstream.managers.ActionManager',
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    'USE_JSONFIELD': False,
}

ACCOUNT_ADAPTER = 'redpanal.users.account_adapter.MyAccountAdapter'

SOCIALACCOUNT_PROVIDERS = {
    'google':
        {'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
         'AUTH_PARAMS': {'access_type': 'online'}}
}

CRISPY_TEMPLATE_PACK = "bootstrap"

SOUTH_TESTS_MIGRATE = False

TEST_RUNNER = 'redpanal.core.tests.RedPanalTestSuiteRunner'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_PATH, 'whoosh_index'),
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

THUMBNAIL_ALIASES = {
    '': {
        'small': {'size': (50, 50), 'crop': True},
        'medium': {'size': (300, 300), 'crop': True},
    },
}
