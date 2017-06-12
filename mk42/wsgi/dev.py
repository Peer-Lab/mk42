# -*- coding: utf-8 -*-

# mk42
# mk42/wsgi/dev.py

from __future__ import unicode_literals
import os

from django.core.wsgi import get_wsgi_application


__all__ = [
    "application",
]


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mk42.settings.dev")
application = get_wsgi_application()
