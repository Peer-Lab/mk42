# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/models/user.py

from __future__ import unicode_literals
import uuid

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.sessions.models import Session
from django.conf import settings

from avatar.templatetags.avatar_tags import avatar_url
from django_countries.fields import CountryField

from mk42.apps.users.managers.user import UserManager


__all__ = [
    "User",
]


class User(AbstractUser):
    """
    Custom user model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"))
    language = models.CharField(verbose_name=_("language"), max_length=5, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)
    country = CountryField(verbose_name=_("country"), blank=True, null=True)

    FIELDS = ["id", "language", "country", ]

    def __unicode__(self):

        return getattr(self, self.USERNAME_FIELD)

    def __str__(self):

        return self.__unicode__()

    class Meta:

        app_label = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    objects = UserManager()

    def kick(self):
        """
        Clear all user sessions (logout from all logged in devices).
        """

        sessions = Session.objects.all()

        for session in sessions:
            if session.get_decoded().get("_auth_user_id") == self.pk:
                session.delete()

    @property
    def avatar(self):
        """
        Return user avatar url.
        
        :return: user avatar url.
        :rtype: unicode.
        """

        return avatar_url(self)
