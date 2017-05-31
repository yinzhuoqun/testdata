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
from django.conf import settings

admin.site.site_title = settings.ADMIN_SITE_TITLE  # 站点标题
admin.site.site_header = settings.ADMIN_SITE_HEADER  # 站点头部

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', index),
    url(r'^$', index),

    url(r'^page/(\d{1,2})', new_page),

    url(r'^login/', login),
    url(r'^id/', testid),
    url(r'^sid/', show_testid),
    url(r'^aid/', alter_testid),
    url(r'^test_change_env/', test_change_env),

    url(r'^app/', app_list),

    url(r'^report/', include('testfly.urls', namespace="testfly")),

    url(r'^testreport/', test_report),
    url(r'^testreport/(Android|iOS)', test_report_platform),
    url(r'^testreport/(Android|iOS)/(\d.\d.\d)', test_report_platform_version),

    url(r'^polls/', include('polls.urls', namespace="polls")),

    url(r'^resume/', resume),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^qqbot/', qqbot_start),

    url(r'^tk/', show_ticket),
    url(r'^appinfo/', app_info),
    url(r'^showappinfo/', show_appinfo),
    url(r'^ud/', device_unlock),
]

# 导入setting、static 是为 media 用
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns = [
#
# # ... the rest of your URLconf goes here ...
#
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
