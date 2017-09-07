# -*- coding: utf-8 -*-

# mk42
# mk42/core/constants.py

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _


__all__ = [
    "LOG_STATUS_PENDING",
    "LOG_STATUS_CANCELED",
    "LOG_STATUS_ONGOING",
    "LOG_STATUS_FINISHED",
    "LOG_STATUS_CHOICES",
]

LOG_STATUS_PENDING, LOG_STATUS_CANCELED, LOG_STATUS_ONGOING, LOG_STATUS_FINISHED = range(1, 5)

LOG_STATUS_CHOICES = (
    (LOG_STATUS_PENDING, _("Pending")),
    (LOG_STATUS_CANCELED, _("Canceled")),
    (LOG_STATUS_ONGOING, _("Ongoing")),
    (LOG_STATUS_FINISHED, _("Finished")),
)
