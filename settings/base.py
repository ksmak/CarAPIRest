# Python
import sys
import os
from pathlib import Path

# Third part
from decouple import config
import pygments.formatters
import mimetypes


mimetypes.add_type("application/javascript", ".js", True)

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(BASE_DIR)

sys.path.append(os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = config('SECRET_KEY', cast=str)

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['*']

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',
    'rest_framework',
]

PROJECT_APPS = [
    'auths.apps.AuthsConfig',
    'tasks.apps.TasksConfig',
    'cars.apps.CarsConfig'
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

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

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'auths.CustomUser'

# Shell plus
SHELL_PLUS = "ipython"

SHELL_PLUS_PRINT_SQL = True

SHELL_PLUS_PYGMENTS_FORMATTER = pygments.formatters.TerminalFormatter

SHELL_PLUS_PYGMENTS_FORMATTER_KWARGS = {}

SHELL_PLUS_PRE_IMPORTS = [
    ('django.db', ('connection', 'connections', 'reset_queries')),
    ('datetime', ('datetime', 'timedelta', 'date')),
    ('json', ('loads', 'dumps'))
]

IPYTHON_KERNEL_DISPLAY_NAME = "Django Shell-Plus"

SHELL_PLUS_MODEL_ALIASES = {
    'auths': {
        'CustomUser': 'U'
    },
    'tasks': {
        'Tasks': 'T',
    },
    'cars': {
        'Car': 'C',
    }
}

# Debug toolbar
DEBUG_TOOLBAR_PATCH_SETTINGS = False

INTERNAL_IPS = [
    "127.0.0.1",
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel'
]