# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/models/event.py


from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

from redactor.fields import RedactorField

from mk42.apps.core.constants import (
    LOG_STATUS_CHOICES,
    LOG_STATUS_PENDING,
    LOG_STATUS_CANCELED,
    LOG_STATUS_ONGOING,
    LOG_STATUS_FINISHED,
)
from mk42.apps.core.validators.event import (
    validate_start,
    validate_end,
)

from mk42.apps.core.signals.event import post_save_event


__all__ = [
    "Event",
]


class Event(models.Model):
    """
    Event model.
    """

    STATUS_PENDING, STATUS_CANCELED, STATUS_ONGOING, STATUS_FINISHED = LOG_STATUS_PENDING, LOG_STATUS_CANCELED, LOG_STATUS_ONGOING, LOG_STATUS_FINISHED
    STATUS_CHOICES = LOG_STATUS_CHOICES

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"))
    name = models.CharField(verbose_name=_("name"), max_length=256, db_index=True, unique=True)
    description = RedactorField(verbose_name=_("description"), blank=True, null=True, db_index=True)
    group = models.ForeignKey("core.Group", verbose_name=_("group"), db_index=True, related_name="events")
    address = models.CharField(verbose_name=_("address"), max_length=2048, blank=False, null=True, db_index=True)
    start = models.DateTimeField(verbose_name=_("start date/time"), blank=False, null=True, db_index=True, validators=[validate_start, ])
    end = models.DateTimeField(verbose_name=_("end date/time"), blank=False, null=True, db_index=True, validators=[validate_end, ])
    created = models.DateTimeField(verbose_name=_("created date/time"), blank=True, null=True, db_index=True, auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("start date/time"), blank=True, null=True, db_index=True, auto_now=True)

    class Meta:

        unique_together = ["group", "start",]
        app_label = "core"
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ["-start"]

    def __unicode__(self):

        return self.name

    def __str__(self):

        return self.__unicode__()

    @property
    def status(self):
        """
        Return event status.

        :return: event status.
        :rtype: int.
        """

        return self.logs.first().status if self.logs.first() else self.STATUS_PENDING

    @property
    def human_readable_status(self):
        """
        Return event status name.

        :return: event status name.
        :rtype: str.
        """

        return dict(self.STATUS_CHOICES).get(self.status, self.STATUS_PENDING)

    def log_pending(self, *args, **kwargs):
        """
        Create event log with status == "mk42.apps.core.models.log.EventLog.STATUS_PENDING".

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: event log model instance with status == "mk42.apps.core.models.log.EventLog.STATUS_PENDING".
        :rtype: mk42.apps.core.models.log.EventLog.
        """

        defaults = {
            "event": self,
            "status": self.STATUS_PENDING,
        }
        condition = not self.logs.exists()

        return self.logs.create(**defaults) if condition else None

    def log_canceled(self, *args, **kwargs):
        """
        Create event log with status == "mk42.apps.core.models.log.EventLog.STATUS_CANCELED".

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: event log model instance with status == "mk42.apps.core.models.log.EventLog.STATUS_CANCELED".
        :rtype: mk42.apps.core.models.log.EventLog.
        """

        defaults = {
            "event": self,
            "status": self.STATUS_CANCELED,
        }
        condition = all([
            not self.logs.filter(status=self.STATUS_ONGOING).exists(),
            self.logs.filter(status=self.STATUS_PENDING).exists(),
        ])

        return self.logs.create(**defaults) if condition else None

    def log_ongoing(self, *args, **kwargs):
        """
        Create event log with status == "mk42.apps.core.models.log.EventLog.STATUS_ONGOING".

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: event log model instance with status == "mk42.apps.core.models.log.EventLog.STATUS_ONGOING".
        :rtype: mk42.apps.core.models.log.EventLog.
        """

        defaults = {
            "event": self,
            "status": self.STATUS_ONGOING,
        }
        condition = all([
            not self.logs.filter(status=self.STATUS_FINISHED).exists(),
            not self.logs.filter(status=self.STATUS_CANCELED).exists(),
            self.logs.filter(status=self.STATUS_PENDING).exists(),
        ])

        return self.logs.create(**defaults) if condition else None

    def log_finished(self, *args, **kwargs):
        """
        Create event log with status == "mk42.apps.core.models.log.EventLog.STATUS_FINISHED".

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: event log model instance with status == "mk42.apps.core.models.log.EventLog.STATUS_FINISHED".
        :rtype: mk42.apps.core.models.log.EventLog.
        """

        defaults = {
            "event": self,
            "status": self.STATUS_FINISHED,
        }
        condition = all([
            not self.logs.filter(status=self.STATUS_FINISHED).exists(),
            not self.logs.filter(status=self.STATUS_CANCELED).exists(),
            self.logs.filter(status=self.STATUS_ONGOING).exists(),
        ])

        return self.logs.create(**defaults) if condition else None


# register signals
post_save.connect(post_save_event, sender=Event)
