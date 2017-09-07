# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/signals/event.py

from __future__ import unicode_literals

from mk42.apps.core.models.log import EventLog


__all__ = [
    "post_save_event",
]


def post_save_event(sender, instance, created, **kwargs):
    """
    Add event status in log on event creation.

    :param sender: sender model class.
    :type sender: object.
    :param instance: group model instance.
    :type instance: mk42.apps.core.models.event.Event.
    :param created: is model instance created/edited.
    :type created: bool
    :param kwargs: additional args.
    :type kwargs: dict.
    """

    if created:
        
        EventLog.objects.get_or_create(event=instance)
