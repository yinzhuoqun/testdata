#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

from django.conf.urls import url
from testfly import views

from testfly import api
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'blogs', api.BlogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.



urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<platform>Android|android|iOS|ios|other)/$', views.Platform, name='platform'),
    url(r'^(?P<platform>Android|android|iOS|ios|other)/(?P<version>(\d.\d.\d))/$', views.Detail, name='detail'),

    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
