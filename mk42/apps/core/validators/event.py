# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/validators/event.py

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

__all__ = [
    "validate_start",
    "validate_end",
]



def validate_start(start):
    """
    Checks if new event starts in the past.

    :param start: event start.
    :type start: datetime.
    """

    if start < timezone.now():

        raise ValidationError(_("Start of new event can't be in the past"))


def validate_end(end):
    """
    Checks if new event ends in the past.

    :param end: event end.
    :type end: datetime.
    """

    if end < timezone.now():
        
        raise ValidationError(_("End of new event can't be in the past"))
