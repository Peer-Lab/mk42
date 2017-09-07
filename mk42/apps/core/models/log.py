# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/models/log.py

from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mk42.apps.core.constants import (
    LOG_STATUS_CHOICES,
    LOG_STATUS_PENDING,
    LOG_STATUS_CANCELED,
    LOG_STATUS_ONGOING,
    LOG_STATUS_FINISHED,
)


__all__ = [
    "EventLog",
]


class EventLog(models.Model):
    """
    EventLog model.
    """

    STATUS_PENDING, STATUS_CANCELED, STATUS_ONGOING, STATUS_FINISHED = LOG_STATUS_PENDING, LOG_STATUS_CANCELED, LOG_STATUS_ONGOING, LOG_STATUS_FINISHED
    STATUS_CHOICES = LOG_STATUS_CHOICES

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"))
    event = models.ForeignKey("core.Event",  verbose_name=_("event"), db_index=True, related_name="logs")
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_PENDING)
    created = models.DateTimeField(verbose_name=_("created date/time"), blank=True, null=True, db_index=True, auto_now_add=True)

    class Meta:

        app_label = "core"
        verbose_name = _("event log")
        verbose_name_plural = _("event logs")
        ordering = ["-created", ]

    def __unicode__(self):

        return "{event}: {status}".format(**{
            "event": self.event,
            "status": self.status,
        })

    def __str__(self):

        return self.__unicode__()
