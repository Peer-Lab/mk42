# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/__init__.py

from __future__ import unicode_literals

from django.contrib import admin

from mk42.apps.core.models.group import Group
from mk42.apps.core.admin.group import GroupAdmin


__all__ = [
    "GroupAdmin",
]


# registering admin custom classes
admin.site.register(Group, GroupAdmin)
