# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/viewsets/event_log.py


from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from mk42.apps.core.models.event import Event
from mk42.apps.core.api.serializers.log import EventLogSerializer
from mk42.apps.core.api.permissions.log import EventLogPermissions
from mk42.lib.utils.pagination import ExtendedPageNumberPagination


__all__ = [
    "EventLogViewSet",
]


class EventLogViewSet(ModelViewSet):
    """
    EventLog view set.
    """

    queryset = EventLog.objects.all() 
    serializer_class = EventLogSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    pagination_class = ExtendedPageNumberPagination
    permission_classes = [EventPermissions, ]
    filter_fields = ["event", ]
    ordering_fields = ["created", "status", ]

