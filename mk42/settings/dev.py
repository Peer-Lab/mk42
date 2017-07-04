# -*- coding: utf-8 -*-

# mk42
# mk42/settings/dev.py

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
DATABASE_ENGINE = env.db().get("ENGINE").split(".")[-1]
DATABASE_NAME = env.db().get("NAME")
DATABASE_USER = env.db().get("USER")
DATABASE_PASSWORD = env.db().get("PASSWORD")
DATABASE_HOST = env.db().get("HOST")
DATABASE_PORT = env.db().get("PORT")

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
REDIS_DB = env.dict("REDIS_URL").get("db")
REDIS_PASSWORD = env.dict("REDIS_URL").get("password")
REDIS_HOST = env.dict("REDIS_URL").get("host")
REDIS_PORT = env.dict("REDIS_URL").get("port")
REDIS_CONNECTION = {
    "db": REDIS_DB,
    "host": REDIS_HOST,
    "port": REDIS_PASSWORD,
    "password": REDIS_PASSWORD,
}

# celery settings
BROKER_URL = env("BROKER_URL")

# e-mail settings
EMAIL_BACKEND = env.email_url().get("EMAIL_BACKEND")
DEFAULT_FROM_EMAIL = env.email_url().get("OPTIONS").get("DEFAULT_FROM_EMAIL")
DEFAULT_FROM_EMAIL_SENDER = env.email_url().get("OPTIONS").get("DEFAULT_FROM_EMAIL_SENDER")

# cache
CACHES = {
    "default": env.cache(),
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
