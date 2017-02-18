"""yzqProgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from xuegod.views import *  # 导入app下views
from testfly.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^page/(\d{1,2})', new_page),
    url(r'^index/', index),
    url(r'^$', index),
    url(r'^login/', login),
    url(r'^id/', testid),
    url(r'^sid/', show_testid),
    url(r'^aid/', alter_testid),
    url(r'^app/', app_list),
    url(r'^testreport/', test_report),
    url(r'^testreport/(Android|iOS)', test_report_platform),
    url(r'^testreport/(Android|iOS)/(\d.\d.\d)', test_report_platform_version),


    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^report/', include('testfly.urls', namespace="testfly")),
]
