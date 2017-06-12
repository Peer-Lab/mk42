# -*- coding: utf-8 -*-

# mk42
# mk42/settings/common.py

from __future__ import unicode_literals
import os

from common import *


ENVIRONMENT = "dev"

DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


WSGI_APPLICATION = "mk42.wsgi.dev.application"

# for old django and django reusable applications config fix
DATABASE_ENGINE = "sqlite3"
DATABASE_NAME = os.path.join(BASE_DIR, "data/db/{name}.sqlite3".format(**{"name": NAME, })).replace("\\", "/")
DATABASE_USER = ""
DATABASE_PASSWORD = ""
DATABASE_HOST = ""
DATABASE_PORT = ""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.{engine}".format(**{"engine": DATABASE_ENGINE, }),
        "NAME": DATABASE_NAME,
        "USER": DATABASE_USER,
        "PASSWORD": DATABASE_PASSWORD,
        "HOST": DATABASE_HOST,
        "PORT": DATABASE_PORT,
    },
}

# redis settings
REDIS_DB = 4
REDIS_PASSWORD = ""
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_CONNECTION = {
    "db": REDIS_DB,
    "host": REDIS_HOST,
    "port": REDIS_PASSWORD,
    "password": REDIS_PASSWORD,
}

# celery settings
BROKER_URL = "amqp://mk42:mk42@localhost:5672/mk42"

# e-mail settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@mk42.local"
DEFAULT_FROM_EMAIL_SENDER = "mk42"

# cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
        "TIMEOUT": 600,
        "KEY_PREFIX": "mk42",
    },
}

INTERNAL_IPS = (
    "127.0.0.1",
)
ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1",
    "localhost",
    "mk42.local",
    "*",
]

# debug toolbar settings
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
]

# thumbnails settings
THUMBNAIL_KVSTORE = "sorl.thumbnail.kvstores.redis_kvstore.KVStore"
THUMBNAIL_REDIS_DB = REDIS_DB
THUMBNAIL_REDIS_PASSWORD = REDIS_PASSWORD
THUMBNAIL_REDIS_HOST = REDIS_HOST
THUMBNAIL_REDIS_PORT = REDIS_PORT

# session settings
SESSION_REDIS_HOST = REDIS_HOST
SESSION_REDIS_PORT = REDIS_PORT
SESSION_REDIS_DB = REDIS_DB
SESSION_REDIS_PASSWORD = REDIS_PASSWORD
SESSION_REDIS_PREFIX = "session"
SESSION_REDIS_SOCKET_TIMEOUT = 1

ROOT_URLCONF = "mk42.urls.dev"
