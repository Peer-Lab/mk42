# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/group.py

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "GroupAdmin",
]


class GroupAdmin(admin.ModelAdmin):
    """
    Customize Group model for admin area.
    """

    list_display = ["id", "name", "owner", "created", "updated", "active", "slug", ]
    list_filter = ["owner", "active", ]
    search_fields = ["id", "name", ]
    date_hierarchy = "created"
    readonly_fields = ["created", "updated", ]
    list_editable = ["active", ]
    fieldsets = (
        [None, {"fields": ["name", "owner", "description", ], }, ],
        [_("Other"), {"fields": ["created", "updated", "active", "slug", ], }, ],
    )
