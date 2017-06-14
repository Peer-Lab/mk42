# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/api/permissions/user.py

from __future__ import unicode_literals

from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)

from mk42.constants import (
    POST,
    DELETE,
    PATCH,
)


__all__ = [
    "UserPermissions",
]


class UserPermissions(BasePermission):
    """
    User permissions.
    """

    def has_permission(self, request, view):
        """
        List/create objects permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.users.api.viewsets.user.UserViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if request.method == POST:
            # Allow create users.
            return True

        if request.method == PATCH:
            # In futures steps of flow allow user edit self.
            return True

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.users.api.viewsets.user.UserViewset.
        :param obj: user model instance.
        :type obj: mk42.apps.users.models.user.User.
        :return: permission is granted.
        :rtype: bool.
        """

        if obj == request.user:
            # Allow only owner edit objects.
            return True

        if request.method == DELETE:
            # Disallow delete users by anyone.
            return False

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True
