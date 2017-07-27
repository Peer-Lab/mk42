# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/models/event_status_log.py

from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from mk42.constants import (
    PENDING,
    CANCELLED,
    ONGOING,
    FINISHED,
)


__all__ = [
    "EventStatusLog",
]


class EventStatusLog(models.Model):
    """
    EventStatusLog model.
    """

    Status = (
        (PENDING, 'Pending'),
        (CANCELLED, 'Canceled'),
        (ONGOING, 'Ongoing'),
        (FINISHED, 'Finished'),
    )


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"))
    event = models.ForeignKey("core.Event",  verbose_name=_("event"), db_index=True, related_name="event status log")
    status = models.IntegerField(choices=Status, default=PENDING)
    created = models.DateTimeField(verbose_name=_("created date/time"), blank=True, null=True, db_index=True, auto_now_add=True)


    class Meta:

        app_label = "core"
        verbose_name = _("event status log")
        verbose_name_plural = _("event status logs")
        ordering = ["-created", ]

    def __unicode__(self):

        return "{event}: {status}".format(**{
            "event": self.event,
            "status": self.status,
        })

    def __str__(self):

        return self.__unicode__()
