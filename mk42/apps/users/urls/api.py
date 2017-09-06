# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/urls/api.py

from __future__ import unicode_literals

from django.conf.urls import (
    url,
    include,
)

from mk42.apps.users.api.routers import router
from mk42.apps.users.api.viewsets.user import UserViewSet


__all__ = [
    "api",
]

# custom endpoints
# user
me = UserViewSet.as_view({"get": "me"})


api = [
    url(r"^api/user/me\.(?P<format>[a-z0-9]+)/?$", me, name="user--me"),
    url(r"^api/user/me/$", me, name="user--me"),
    url(r"^api/", include(router.urls)),
]
