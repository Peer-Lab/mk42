# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/serializers/event_log.py

from __future__ import unicode_literals

from rest_framework import serializers

from mk42.apps.core.models.event_log import EventLog


__all__ = [
    "EventLogSerializer",
]


class EventLogSerializer(serializers.ModelSerializer):
    """
    EventLog serializer.
    """

    class Meta:

        model = EventLog
        read_only_fields = [
            "created",
        ]
        extra_kwargs = {
            "url": {"view_name": "core:eventlog-detail", },
        }
        fields = [
            "id",
            "event",
            "status",
            "created",
            "url",
        ]
