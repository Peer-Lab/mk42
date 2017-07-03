# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/event.py

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "EventAdmin",
]


class EventAdmin(admin.ModelAdmin):
    """
    Customize Event model for admin area.
    """

    list_display = ["id", "name", "description", "group", "start", "created", "updated", ]
    list_filter = ["group", "created", "start" ]
    search_fields = ["id", "name", "start" ]
    date_hierarchy = "created"
    readonly_fields = ["created", "updated", ]
    fieldsets = (
        [None, {"fields": ["name", "description", "group",], }, ],
        [_("Other"), {"fields": ["created", "updated", ], }, ],
    )


