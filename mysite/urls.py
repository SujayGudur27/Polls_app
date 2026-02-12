from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path("", lambda request: redirect("polls/")),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
