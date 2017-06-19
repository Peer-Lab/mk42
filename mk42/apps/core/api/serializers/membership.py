# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/serializers/membership.py

from __future__ import unicode_literals

from rest_framework import serializers

from mk42.apps.core.models.membership import Membership


__all__ = [
    "MembershipSerializer",
]


class MembershipSerializer(serializers.ModelSerializer):
    """
    Membership serializer.
    """

    class Meta:

        model = Membership
        read_only_fields = [
            "created",
        ]
        extra_kwargs = {
            "url": {"view_name": "core:membership-detail", },
        }
        fields = [
            "id",
            "user",
            "group",
            "created",
            "url",
        ]
