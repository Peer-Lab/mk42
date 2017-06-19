# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/__init__.py

from __future__ import unicode_literals

from django.contrib import admin

from mk42.apps.core.models.group import Group
from mk42.apps.core.models.membership import Membership
from mk42.apps.core.admin.group import GroupAdmin
from mk42.apps.core.admin.membership import MembershipAdmin


__all__ = [
    "GroupAdmin",
    "MembershipAdmin",
]


# registering admin custom classes
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
