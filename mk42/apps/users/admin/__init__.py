# mk42
# mk42/apps/users/admin/__init__.py

from __future__ import unicode_literals

from django.contrib import admin

from mk42.apps.users.models.user import User
from mk42.apps.users.admin.user import UserAdmin


__all__ = [
    "UserAdmin",
]


# register admin custom classes
admin.site.register(User, UserAdmin)
