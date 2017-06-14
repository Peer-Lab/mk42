# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/api/viewsets/user.py

from __future__ import unicode_literals

from django.contrib.gis.geoip import GeoIP
from django.utils.translation import get_language

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django_filters.rest_framework import DjangoFilterBackend

from mk42.apps.users.models.user import User
from mk42.apps.users.api.serializers.user import UserSerializer
from mk42.apps.users.api.permissions.user import UserPermissions
from mk42.apps.users.api.filters.user import UserFilter
from mk42.lib.utils.pagination import ExtendedPageNumberPagination


__all__ = [
    "UserViewSet",
]


class UserViewSet(ModelViewSet):
    """
    User view set.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]
    pagination_class = ExtendedPageNumberPagination
    filter_class = UserFilter
    permission_classes = [UserPermissions, ]
    filter_fields = ["id", "is_active", "language", "country", ]
    ordering_fields = ["id", "is_active", ]
    search_fields = ["id", ]

    def perform_create(self, serializer):
        """
        Override to set user country and language.

        :param serializer: instance of user model serializer.
        :type serializer: mk42.apps.users.api.serializers.user.UserSerializer.
        """

        defaults = {
            "country": GeoIP().country(self.request.META.get("REMOTE_ADDR", None)).get("country_code",""),
            "language": get_language(),
        }

        serializer.save(**defaults)
