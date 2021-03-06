# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin

from cruds.urls import (
    crud_for_model,
)
from .models import Author, Country


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


# add crud for whole app
urlpatterns += crud_for_model(Author, urlprefix='testapp/')
urlpatterns += crud_for_model(Country, urlprefix='testapp/')
