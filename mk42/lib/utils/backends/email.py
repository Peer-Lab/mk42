# -*- coding: utf-8 -*-

# mk42
# mk42/backends/email.py

from __future__ import unicode_literals

from djcelery_email.backends import CeleryEmailBackend
from templated_email.backends.vanilla_django import TemplateBackend


__all__ = [
    "CeleryTemplateEmailBackend",
]


class CeleryTemplateEmailBackend(CeleryEmailBackend, TemplateBackend):
    """
    Custom email backend using celery to send HTML emails.
    """

    pass
