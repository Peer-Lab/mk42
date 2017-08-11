# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/log.py

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "EventLogAdmin",
]


class EventLogAdmin(admin.ModelAdmin):
    """
    Customize EventLog model for admin area.
    """

    list_display = ["id", "event", "status", "created", ]
    list_filter = ["event", "status"]
    date_hierarchy = "created"
    readonly_fields = ["created", ]
    fieldsets = (
        [None, {"fields": ["event", "status", ], }, ],
        [_("Other"), {"fields": ["created", ], }, ],
    )
