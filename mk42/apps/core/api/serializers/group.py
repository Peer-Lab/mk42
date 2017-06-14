# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/serializers/group.py

from __future__ import unicode_literals

from rest_framework import serializers

from mk42.apps.core.models.group import Group


__all__ = [
    "GroupSerializer",
]


class GroupSerializer(serializers.ModelSerializer):
    """
    Group serializer.
    """

    class Meta:

        model = Group
        read_only_fields = [
            "created",
            "updated",
            "active",
            "slug",
        ]
        extra_kwargs = {
            "url": {"view_name": "core:group-detail", },
        }
        fields = [
            "id",
            "name",
            "slug",
            "owner",
            "description",
            "created",
            "updated",
            "active",
            "url",
        ]
