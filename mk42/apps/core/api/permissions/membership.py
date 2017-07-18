# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/permissions/membership.py

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
from mk42.apps.core.models.membership import Membership


__all__ = [
    "MembershipPermissions",
]


class MembershipPermissions(BasePermission):
    """
    Membership permissions.
    """

    def has_permission(self, request, view):
        """
        List/create objects permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.core.api.viewsets.membership.MembershipViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if all([request.method == POST, is_authenticated(request.user), ]):
            # Allow join to groups only for authenticated users.
            return True

        if request.method == DELETE:
            # In futures steps of flow allow user delete own membership.
            return True

        if request.method == PATCH:
            # In futures steps of flow allow owner of group to activate membership
            return True

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.core.api.viewsets.membership.MembershipViewset.
        :param obj: membership model instance.
        :type obj: mk42.apps.core.models.membership.Membership.
        :return: permission is granted.
        :rtype: bool.
        """

        if all([obj.user == request.user, request.method == DELETE, ]):
            # Allow only delete membership.
            return True

        if all([request.method == PATCH, request.user == obj.group.owner, ]):
            # Allow only membership group owner edit user membership (activate it).
            return True

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True
