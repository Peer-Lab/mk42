# -*- coding: utf-8 -*-

# mk42
# mk42/apps/user/api/filters/user.py

from __future__ import unicode_literals

from django_filters.rest_framework import FilterSet

from mk42.apps.users.models.user import User


__all__ = [
    "UserFilter",
]


class UserFilter(FilterSet):
    """
    User filter.
    """

    class Meta:

        model = User
        fields = ["id", "is_active", "language", "country", ]
