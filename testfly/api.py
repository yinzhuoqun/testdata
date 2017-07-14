#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

# 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
import logging

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)


from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from testfly import models
from rest_framework import response


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Blog
        depth = 1
        fields = ('url', 'title', 'author', 'content')


class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = BlogSerializer