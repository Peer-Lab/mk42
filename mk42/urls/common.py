# -*- coding: utf-8 -*-

# mk42
# mk42/urls/common.py

from __future__ import unicode_literals

from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import javascript_catalog

from rest_framework.authtoken.views import obtain_auth_token
from django_js_reverse.views import urls_js

from mk42.views.base import Index


__all__ = [
    "urlpatterns",
]


urlpatterns = []
JS_I18N_PACKAGES = []

# third part apps urls patterns
urlpatterns += [
    url(r"^robots\.txt", include("robots.urls")),
    url(r"^redactor/", include("redactor.urls")),
    url(r"^get-api-token/", obtain_auth_token, name="get-api-token"),
    url(r"^reverse\.js$", urls_js, name="js-reverse"),
]

# third part apps i18n urls patterns
urlpatterns += i18n_patterns(
    url(r"^get-api-token/", obtain_auth_token, name="get-api-token"),
)

# django urls patterns
urlpatterns += [
    url(r"^i18n/", include("django.conf.urls.i18n")),
]

# django i18n urls patterns
urlpatterns += i18n_patterns(
    url(r"^admin/", include(admin.site.urls)),
    url(r"^i18n\.js$", javascript_catalog, {"domain": "djangojs", "packages": JS_I18N_PACKAGES, }, name="jsi18n"),
)

# mk42 urls patterns
urlpatterns += [
    url(r"^$", Index.as_view(), name="index"),  # index
]

# mk42 i18n urls patterns
urlpatterns += i18n_patterns(
    url(r"^$", Index.as_view(), name="index"),  # index
    url(r"^users/", include("mk42.apps.users.urls", namespace="users", app_name="users")),  # users app
    url(r"^core/", include("mk42.apps.core.urls", namespace="core", app_name="core")),  # core app
)
