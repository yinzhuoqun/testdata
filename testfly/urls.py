#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

from django.conf.urls import url
from testfly import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<platform>Android|iOS|other)/$', views.Platform, name='platform'),
    url(r'^(?P<platform>Android|iOS|other)/(?P<version>(\d.\d.\d))/$', views.Detail, name='detail'),

    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
