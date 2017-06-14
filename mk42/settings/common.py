# -*- coding: utf-8 -*-

# mk42
# mk42/settings/common.py

from __future__ import unicode_literals
import os
import sys
from collections import OrderedDict

from kombu import Queue
import environ

import djcelery

from mk42.version import (
    __version__,
    __updated__,
)


env = environ.Env()

NAME = "mk42"
ENVIRONMENT = ""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).replace("\\", "/")
sys.path.insert(0, BASE_DIR)

SECRET_KEY = env("SECRET_KEY")

# apps
INSTALLED_APPS = [
    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    # third part
    "sitemetrics",
    "djcopyright",
    "robots",
    "corsheaders",
    "djversion",
    "djcelery_email",
    "djcelery",
    "sorl.thumbnail",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "redactor",
    "django_countries",
    "avatar",
    "crispy_forms",
    "templated_email",
    "constance",
    "constance.backends.database",
    "watson",
    # mk42 libs
    # mk42
    "mk42.apps.users",
    "mk42.apps.core",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # must go first of "django.middleware.common.CommonMiddleware"
    # django
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # third part
    # mk42
    "mk42.lib.utils.middleware.StripLanguagePrefix",
]
APPEND_SLASH = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, NAME, "templates").replace("\\", "/"),
        ],
        "APP_DIRS": False,
        "OPTIONS": {
            "context_processors": [
                # django
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # third part
                "constance.context_processors.config",
                # mk42
            ],
            "loaders": [
                # django
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
                "django.template.loaders.eggs.Loader",
                # third part
                # mk42
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
]

# i18n/l10n settings
LANGUAGE_CODE = "en"
gettext = lambda s: s
LANGUAGES = (
    ("en", "English"),
    ("uk", "Українська"),
)
DEFAULT_LANGUAGE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (
    os.path.join(BASE_DIR, NAME, "locale").replace("\\", "/"),
)

# static/media settings
MEDIA_ROOT = os.path.join(BASE_DIR, "media").replace("\\", "/")
STATIC_ROOT = os.path.join(BASE_DIR, "static").replace("\\", "/")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, NAME, "static").replace("\\", "/"),
)
STATICFILES_FINDERS = (
    # django
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # third part
)
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# django copyright settings
DJCOPYRIGHT_START_YEAR = 2017

# celery settings
djcelery.setup_loader()
CELERY_BACKEND = "amqp"
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_MAX_TASKS_PER_CHILD = 5
CELERY_DISABLE_RATE_LIMITS = True
CELERY_ACCEPT_CONTENT = ["pickle", "json", "msgpack", "yaml", ]
CELERY_RESULT_BACKEND = "rpc"
CELERY_TASK_RESULT_EXPIRES = 60  # 1 minute
CELERY_CREATE_MISSING_QUEUES = True
CELERY_DEFAULT_QUEUE = "default"
CELERY_QUEUES = (
    Queue(str("default"), routing_key=str("task.#")),
    Queue(str("email"), routing_key=str("email.#")),
    Queue(str("core"), routing_key=str("core.#")),
)
CELERY_DEFAULT_EXCHANGE = "tasks"
CELERY_DEFAULT_EXCHANGE_TYPE = "topic"
CELERY_DEFAULT_ROUTING_KEY = "task.default"
CELERY_ROUTES = {
    # third part
    "djcelery_email.tasks.djcelery_email_send_multiple": {
        "queue": "email",
        "routing_key": "email.djcelery_email_send_multiple",
    },
    # mk42
}

# email settings
EMAIL_BACKEND = "mk42.lib.utils.backends.email.CeleryTemplateEmailBackend"
CELERY_EMAIL_TASK_CONFIG = {
    "queue": "email",
    "rate_limit": "30/m",
}

# version
DJVERSION_VERSION = __version__
DJVERSION_UPDATED = __updated__

# auth settings
AUTH_USER_MODEL = "users.User"

# site framework settings
SITE_ID = 1

# django messages settings
MESSAGE_STORAGE = "django.contrib.messages.storage.fallback.FallbackStorage"

# autoslug settings
AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"

# thumbnail settings
THUMBNAIL_FORMAT = "PNG"

# api settings
REST_FRAMEWORK = {
    "PAGE_SIZE": 9999,
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
    ],
}

# redactor settings
REDACTOR_UPLOAD = "uploads/"

# session settings
SESSION_ENGINE = "redis_sessions.session"

# GeoIP settings
GEOIP_PATH = os.path.join(BASE_DIR, "data/GeoIP/")

# constance settings
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_DATABASE_CACHE_BACKEND = "default"
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_CONFIG = OrderedDict({})

# robots settings
ROBOTS_USE_SITEMAP = True

# cors settings
CORS_URLS_REGEX = r"/.*?/api/.*?$"
