# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/serializers/event.py

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from mk42.apps.core.models.event import Event


__all__ = [
    "EventSerializer",
]


class EventSerializer(serializers.ModelSerializer):
    """
    Event serializer.
    """

    status = serializers.ReadOnlyField(label=_("status"))

    class Meta:

        model = Event
        read_only_fields = [
            "status",
            "created", 
            "updated",
        ]
        extra_kwargs = {
            "url": {"view_name": "core:event-detail", },
        }
        fields = [
            "id",
            "name",
            "description",
            "group",
            "address",
            "status",
            "start",
            "end",
            "created",
            "updated",
            "url",
        ]
