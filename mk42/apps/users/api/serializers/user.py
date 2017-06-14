# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/api/serializers/user.py

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from django_countries.serializer_fields import CountryField

from mk42.apps.users.models.user import User


__all__ = [
    "UserSerializer",
]


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer.
    """

    full_name = serializers.ReadOnlyField(label=_("full name"), source="get_full_name")
    short_name = serializers.ReadOnlyField(label=_("short name"), source="get_short_name")
    country = CountryField(read_only=True, label=_("country"), country_dict=True)

    class Meta:

        model = User
        read_only_fields = [
            "is_staff",
            "is_superuser",
            "is_active",
            "date_joined",
            "avatar",
            "full_name",
            "short_name",
        ]
        extra_kwargs = {
            "url": {"view_name": "users:user-detail", },
            model.USERNAME_FIELD: {"required": True, },
            "email": {"required": True, },
            "password": {"write_only": True},
        }
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "short_name",
            "is_active",
            "date_joined",
            "avatar",
            model.USERNAME_FIELD,
            "email",
            "password",
            "country",
            "language",
            "url",
        ]

    def post_save(self, obj, created=False):
        """
        On creation, replace the raw password with a hashed version.

        :param obj: user model instance.
        :type obj: mk42.apps.users.models.user.User.
        :param created: is object created.
        :type created: bool.
        """

        if created:
            obj.set_password(obj.password)
            obj.save()
