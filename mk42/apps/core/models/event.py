# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/models/event.py


from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
#from django.db.models.signals import post_save

from redactor.fields import RedactorField

#from mk42.apps.core.managers.group import GroupManager
#from mk42.apps.core.signals.group import post_save_group


__all__ = [
    "Event",
]


class Event(models.Model):
    """
    Event model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"))
    name = models.CharField(verbose_name=_("name"), max_length=256, db_index=True, unique=True)
    description = RedactorField(verbose_name=_("description"), blank=True, null=True, db_index=True)
    group = models.ForeignKey("core.Group", verbose_name=_("group"), db_index=True, related_name="events")
    start = models.DateTimeField(verbose_name=_("start date/time"), blank=True, null=True, db_index=True, auto_now=True)
    created = models.DateTimeField(verbose_name=_("created date/time"), blank=True, null=True, db_index=True, auto_now_add=True)

    #objects = GroupManager()

    class Meta:

        app_label = "core"
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ["-created", "-start"]

    def __unicode__(self):

        return self.name

    def __str__(self):

        return self.__unicode__()


# register signals
#post_save.connect(post_save_group, sender=Group)