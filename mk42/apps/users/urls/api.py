# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/urls/api.py

from __future__ import unicode_literals

from django.conf.urls import (
    url,
    include,
)

from rest_framework.schemas import get_schema_view

from mk42.apps.users.api.routers import router


__all__ = [
    "api",
]


api = [
    url(r"^api/schema/$", get_schema_view(title="Users API")),
    url(r"^api/", include(router.urls)),
]
