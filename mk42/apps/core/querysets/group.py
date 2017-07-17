# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/querysets/groups.py

from __future__ import unicode_literals

from django.db import models


__all__ = [
    "GroupQuerySet",
]


class GroupQuerySet(models.QuerySet):
    """
    Group model queryset.
    """

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

        return self.filter(active=True)
