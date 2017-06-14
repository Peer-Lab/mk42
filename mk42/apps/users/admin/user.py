# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/admin/user.py

from __future__ import unicode_literals
from copy import copy

from django.contrib.auth.admin import UserAdmin as Admin
from django.utils.translation import ugettext_lazy as _

from mk42.apps.users.models.user import User


__all__ = [
    "UserAdmin",
]


class UserAdmin(Admin):
    """
    Customize User model for admin area.
    """

    def __init__(self, *args, **kwargs):
        """
        Override to populate fieldsets.
        """

        super(UserAdmin, self).__init__(*args, **kwargs)
        fields = list(Admin.fieldsets[1][1]["fields"])

        for field in copy(User.FIELDS):
            fields.append(field)

        Admin.fieldsets[1][1]["fields"] = fields

    list_display = ["id", "email", "is_staff", "is_active", "language", "country", ]
    filter_horizontal = ["groups", "user_permissions", ]
    list_filter = ["is_staff", "is_superuser", "is_active", "language", "country", ]
    search_fields = ["id", "email", "first_name", "last_name", ]
    actions = ["kick", ]

    fieldsets = (
        [None, {"fields": ["username", "password", ]}],
        [_("Personal info"), {"fields": ["first_name", "last_name", "email", ]}],
        [_("Permissions"), {"fields": ["is_active", "is_staff", "is_superuser", "groups", "user_permissions", ]}],
        [_("Important dates"), {"fields": ["last_login", "date_joined", ]}],
        [_("Settings"), {"fields": ["language", "country", ]}],
    )

    ordering = ["-date_joined", ]
    date_hierarchy = "date_joined"

    def kick(self, request, queryset):
        """
        Logout selected users.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param queryset: queryset with selected users.
        :type queryset: django.db.models.query.QuerySet.
        """

        for user in queryset:
            user.kick()

    kick.short_description = _("Clear all selected users sessions (logout from all logged in devices) (can take very long time)")
