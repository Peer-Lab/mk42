# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/querysets/membership.py

from __future__ import unicode_literals

from django.db import models


__all__ = [
    "MembershipQuerySet",
]


class MembershipQuerySet(models.QuerySet):
    """
    Membership model queryset.
    """

    def active(self, *args, **kwargs):
        """
        Return active memberships.

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: queryset with active memberships.
        :rtype: django.db.models.query.QuerySet.
        """

        return self.filter(active=True)
