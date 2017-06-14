# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/urls/api.py

from __future__ import unicode_literals

from django.conf.urls import (
    url,
    include,
)

from mk42.apps.users.api.routers import router


__all__ = [
    "api",
]


api = [
    url(r"^api/", include(router.urls)),
]
