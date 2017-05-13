#!/usr/bin/env python
# coding: utf-8
"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

import app.views


urlpatterns = [
    url(r'^django-datatable/datasource/model/$', app.views.base, name='base'),
    url(r'^django-datatable/datasource/ajax/$', app.views.ajax, name='ajax'),
    url(r'^django-datatable/datasource/ajaxsource/$', app.views.ajax_source, name='ajax_source'),
    url(r'^django-datatable/datasource/ajaxsource/api/$', app.views.MyDataView.as_view(), name='ajax_source_api'),

    url(r'^django-datatable/column/sequence/$', app.views.sequence_column, name='sequence_column'),
    url(r'^django-datatable/column/calendar/$', app.views.calendar_column, name='calendar_column'),
    url(r'^django-datatable/column/link/$', app.views.link_column, name='link_column'),
    url(r'^django-datatable/column/checkbox/$', app.views.checkbox_column, name='checkbox_column'),

    url(r'^django-datatable/extensions/buttons/$', app.views.buttons_extension, name='buttons_extension'),

    url(r'^django-datatable/user/(\d+)/$', app.views.user_profile, name='user_profile'),
    url(r'^django-datatable/table/', include('table.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
