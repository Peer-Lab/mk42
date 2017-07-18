# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/managers/group.py

from __future__ import unicode_literals

from django.db import models

from mk42.apps.core.querysets.group import GroupQuerySet


__all__ = [
    "GroupManager",
]


class GroupManager(models.Manager):
    """
    Group model manager.
    """

    def get_queryset(self):
        """
        Override to return custom queryset.

        :return: Group model queryset instance.
        :rtype: mk42.apps.core.querysets.group.GroupQuerySet.
        """

        return GroupQuerySet(self.model, using=self._db)

    def active(self, *args, **kwargs):
        """
        Return active groups.

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: queryset with active groups.
        :rtype: django.db.models.query.QuerySet.
        """

        return self.get_queryset().active(*args, **kwargs)

    def inactive(self, *args, **kwargs):
        """
        Return inactive groups.

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: queryset with inactive groups.
        :rtype: django.db.models.query.QuerySet.
        """

        return self.get_queryset().inactive(*args, **kwargs)
