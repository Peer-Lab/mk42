# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/apps.py

from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "Config",
]


class Config(AppConfig):
    """
    Core app config.
    """

    name = "mk42.apps.core"
    verbose_name = _("Core")
