# -*- coding: utf-8 -*-

# mk42
# mk42/urls/dev.py

from __future__ import unicode_literals

from django.conf.urls import include
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

import debug_toolbar

from mk42.urls.common import urlpatterns


# debugging and development urls hooks
urlpatterns += [
    url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT, "show_indexes": True, }),
]

urlpatterns += [
    url(r"^__debug__/", include(debug_toolbar.urls)),
]
