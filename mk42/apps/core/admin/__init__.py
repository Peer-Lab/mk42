# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/__init__.py

from __future__ import unicode_literals

from django.contrib import admin

from mk42.apps.core.models.group import Group
from mk42.apps.core.models.membership import Membership
from mk42.apps.core.models.event import Event
from mk42.apps.core.models.rsvp import RSVP
from mk42.apps.core.models.log import EventLog

from mk42.apps.core.admin.group import GroupAdmin
from mk42.apps.core.admin.membership import MembershipAdmin
from mk42.apps.core.admin.event import EventAdmin
from mk42.apps.core.admin.rsvp import RSVPAdmin
from mk42.apps.core.admin.log import EventLogAdmin




__all__ = [
    "GroupAdmin",
    "MembershipAdmin",
    "EventAdmin",
    "RSVPAdmin",
    "EventLogAdmin",
]


# registering admin custom classes
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(RSVP, RSVPAdmin)
admin.site.register(EventLog, EventLogAdmin)
