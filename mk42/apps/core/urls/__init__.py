# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/urls/__init__.py

from __future__ import unicode_literals

from mk42.apps.core.urls.api import api


__all__ = [
    "urlpatterns",
]


urlpatterns = []
# merge urlpatterns
urlpatterns += api
