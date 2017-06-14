# -*- coding: utf-8 -*-

# mk42
# mk42/lib/utils/pagination.py

from __future__ import unicode_literals
from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


__all__ = [
    "ExtendedPageNumberPagination",
]


class ExtendedPageNumberPagination(PageNumberPagination):
    """
    Extended page number API pagination class.
    """

    page_size = 9999
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        """
        Return response with some additional fields.

        :param data: data queryset.
        :type data: django.db.models.query.QuerySet.
        :return: extended django rest framework response.
        :rtype: rest_framework.response.Response.
        """

        return Response(OrderedDict([
            ("page", self.page.number),
            ("num_pages", self.page.paginator.num_pages),
            ("count", self.page.paginator.count),
            ("next", self.get_next_link()),
            ("next_page_number", self.page.next_page_number() if self.page.has_next() else None),
            ("previous", self.get_previous_link()),
            ("previous_page_number", self.page.previous_page_number() if self.page.has_previous() else None),
            ("request", self.request.GET),
            ("results", data),
        ]))
