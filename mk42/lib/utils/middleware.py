# -*- coding: utf-8 -*-

# mk42
# mk42/lib/utils/middleware.py

from __future__ import unicode_literals

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


__all__ = [
    "StripLanguagePrefix",
]


class StripLanguagePrefix(MiddlewareMixin):
    """
    Add "no_lang_path" variable to request.session that contains request.path without language prefix.
    """

    def process_request(self, request):
        """
        Modify request.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        """
        l_path = request.path.split("/")
        request.session["no_lang_path"] = request.path

        if l_path[1] in list(dict(settings.LANGUAGES).keys()):
            del l_path[1]
            no_lang_path = "/".join(l_path)
            request.session["no_lang_path"] = no_lang_path
