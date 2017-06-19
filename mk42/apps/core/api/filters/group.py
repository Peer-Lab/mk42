# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/filters/group.py

from __future__ import unicode_literals

from django_filters.rest_framework import FilterSet

from mk42.apps.core.models.group import Group


__all__ = [
    "GroupFilter",
]


class GroupFilter(FilterSet):
    """
    Group filter.
    """

    class Meta:

        model = Group
        fields = ["active", "owner", ]
