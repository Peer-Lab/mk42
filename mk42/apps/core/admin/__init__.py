# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/__init__.py

from __future__ import unicode_literals

from django.contrib import admin

from mk42.apps.core.models.group import Group
from mk42.apps.core.models.membership import Membership
from mk42.apps.core.models.event import Event
from mk42.apps.core.admin.group import GroupAdmin
from mk42.apps.core.admin.membership import MembershipAdmin
from mk42.apps.core.admin.event import EventAdmin



__all__ = [
    "GroupAdmin",
    "MembershipAdmin",
    "EventAdmin",
]


# registering admin custom classes
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Event, EventAdmin)
