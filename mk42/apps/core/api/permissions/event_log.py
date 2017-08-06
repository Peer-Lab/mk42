# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/permissions/event_log.py

from __future__ import unicode_literals

from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)
from rest_framework.compat import is_authenticated

from mk42.constants import (
    POST,
    DELETE,
    PATCH,
)

from mk42.apps.core.models.event import Event


__all__ = [
    "EventLogPermissions",
]


class EventLogPermissions(BasePermission):
    """
    EventLog permissions.
    """

    def check_event_owner(self, request):
    	"""
		Check if user that sends request is event owner.

		:param requeset: django request instance.
		:type request: django.http.request.HttpRequest.
		:return: user is owner.
		:rtype: bool.

    	"""
    	event_id = request.POST["event"]
    	event = Event.object.get(id=event_id)
    	if event.owner == request.user:
    		return True

    def has_permission(self, request, view):
        """
        List/create objects permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.core.api.viewsets.event_log.EventLogViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if all([request.method == POST, is_authenticated(request.user), self.check_event_owner(request)]):
            # Allow add new status only for authenticated users.
            return True

        if request.method == PATCH:
            # In futures steps of flow allow user edit self owned events.
            return False

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.core.api.viewsets.event_log.EventLogViewset.
        :param obj: event_log model instance.
        :type obj: mk42.apps.core.models.event_log.EventLog.
        :return: permission is granted.
        :rtype: bool.
        """


        if request.method == DELETE:
            # Disallow delete events by anyone.
            return False

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True
