# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/api/routers.py

from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from mk42.apps.users.api.viewsets.user import UserViewSet


router = DefaultRouter()

# registering viewsets
router.register(r"user", UserViewSet)
