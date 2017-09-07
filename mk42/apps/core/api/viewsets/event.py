# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/viewsets/event.py

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import detail_route
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from mk42.apps.core.models.event import Event
from mk42.apps.core.api.serializers.event import EventSerializer
from mk42.apps.core.api.permissions.event import EventPermissions
from mk42.lib.utils.pagination import ExtendedPageNumberPagination
from mk42.constants import POST
from mk42.apps.core.api.serializers.log import EventLogSerializer


__all__ = [
    "EventViewSet",
]


class EventViewSet(ModelViewSet):
    """
    Event view set.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    pagination_class = ExtendedPageNumberPagination
    permission_classes = [EventPermissions, ]
    filter_fields = ["group", ]
    ordering_fields = ["created", "start", ]

    @detail_route(methods=[POST, ], url_path="log/pending")
    def log_pending(self, request, pk=None, **kwargs):
        """
        Create event log with status == "mk42.apps.core.constants.STATUS_PENDING". Actually NO.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param pk: event object primary key.
        :type pk: unicode.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: django rest framework response.
        :rtype: rest_framework.response.Response.
        """

        raise PermissionDenied(detail=_("Okay move along, move along people, there's nothing to see here!"))

    @detail_route(methods=[POST, ], url_path="log/canceled")
    def log_canceled(self, request, pk=None, **kwargs):
        """
        Create event log with status == "mk42.apps.core.constants.STATUS_CANCELED".

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param pk: event object primary key.
        :type pk: unicode.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: django rest framework response.
        :rtype: rest_framework.response.Response.
        """

        obj = self.get_object()

        if request.user != obj.group.owner:
            # only group owner can change event status
            raise PermissionDenied(detail=_("You must be owner of this group to perform this action."))

        log = obj.log_canceled(**kwargs)

        if not log:
            # can't create event logs with status == "mk42.apps.core.constants.STATUS_CANCELED"
            # if log with status == "mk42.apps.core.constants.STATUS_PENDING" does not exist
            # or log with status == "mk42.apps.core.constants.STATUS_ONGOING" exist
            raise PermissionDenied(detail=_("Can't change status to '{status}'.").format(**{"status": dict(obj.STATUS_CHOICES).get(obj.STATUS_CANCELED), }))

        return Response({"detail": EventLogSerializer(instance=log, context={"request": request, }).data if log else None, })

    @detail_route(methods=[POST, ], url_path="log/ongoing")
    def log_ongoing(self, request, pk=None, **kwargs):
        """
        Create event log with status == "mk42.apps.core.constants.STATUS_ONGOING".

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param pk: event object primary key.
        :type pk: unicode.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: django rest framework response.
        :rtype: rest_framework.response.Response.
        """

        obj = self.get_object()

        if request.user != obj.group.owner:
            # only group owner can change event status
            raise PermissionDenied(detail=_("You must be owner of this group to perform this action."))

        log = obj.log_ongoing(**kwargs)

        if not log:
            # can't create event logs with status == "mk42.apps.core.constants.STATUS_ONGOING"
            # if log with status == "mk42.apps.core.constants.STATUS_FINISHED" exist
            # if log with status == "mk42.apps.core.constants.STATUS_CANCELED" exist
            # or log with status == "mk42.apps.core.constants.STATUS_PENDING" does not exist
            raise PermissionDenied(detail=_("Can't change status to '{status}'.").format(**{"status": dict(obj.STATUS_CHOICES).get(obj.STATUS_ONGOING), }))

        return Response({"detail": EventLogSerializer(instance=log, context={"request": request, }).data if log else None, })

    @detail_route(methods=[POST, ], url_path="log/finished")
    def log_finished(self, request, pk=None, **kwargs):
        """
        Create event log with status == "mk42.apps.core.constants.STATUS_FINISHED".

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param pk: event object primary key.
        :type pk: unicode.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: django rest framework response.
        :rtype: rest_framework.response.Response.
        """

        obj = self.get_object()

        if request.user != obj.group.owner:
            # only group owner can change event status
            raise PermissionDenied(detail=_("You must be owner of this group to perform this action."))

        log = obj.log_finished(**kwargs)

        if not log:
            # can't create event logs with status == "mk42.apps.core.constants.STATUS_FINISHED"
            # if log with status == "mk42.apps.core.constants.STATUS_FINISHED" exist
            # if log with status == "mk42.apps.core.constants.STATUS_CANCELED" exist
            # or log with status == "mk42.apps.core.constants.STATUS_ONGOING" does not exist
            raise PermissionDenied(detail=_("Can't change status to '{status}'.").format(**{"status": dict(obj.STATUS_CHOICES).get(obj.STATUS_FINISHED), }))

        return Response({"detail": EventLogSerializer(instance=log, context={"request": request, }).data if log else None, })
