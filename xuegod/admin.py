# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from django.apps import AppConfig
from xuegod.models import *


# @admin.register( TestId ) # 注册方法1
class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'alimysql'  # 数据库
    list_display = ('id', 'user_id', 'user_password', 'user_note', 'user_flag')  # 展示列表项
    list_filter = ['user_flag']  # 过滤器
    search_fields = ['user_id']  # 搜索框
    list_display_links = ('id', 'user_id', 'user_password')

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(MultiDBModelAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(db_field, request=request, using=self.using,
                                                                       **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(db_field, request=request, using=self.using,
                                                                       **kwargs)


class MultiDBTabularInline(admin.TabularInline):
    # class MultiDBTabularInline(admin.ModelAdmin):
    using = 'alimysql'
    list_display = ('user_id', 'user_password', 'user_note', 'user_flag')

    def get_queryset(self, request):
        # Tell Django to look for inline objects on the 'other' database.
        return super(MultiDBTabularInline, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(MultiDBTabularInline, self).formfield_for_foreignkey(db_field, request=request, using=self.using,
                                                                          **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(MultiDBTabularInline, self).formfield_for_manytomany(db_field, request=request, using=self.using,
                                                                          **kwargs)


# 指定数据库  # 注册方法2
admin.site.register(TestId, MultiDBModelAdmin)


class TestParticipantsInline(admin.TabularInline):
    model = TestParticipants  # 模型名称
    extra = 1  # 默认数量


class BugSurplusInfoInline(admin.TabularInline):
    model = BugSurplusInfo
    extra = 1  # 默认数量


class BugInfoInline(admin.TabularInline):
    model = BugInfo
    extra = 1  # 默认数量


class TestReportAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'test_version', 'test_platform')  # 展示的列
    list_filter = ['test_platform']  # 过滤
    search_fields = ['test_version']  # 搜索
    # fieldsets = [
    #     ("BUG 信息", {'fields': [""]}),
    #     ("参与人员", {'fields:['']'})
    # ]
    #
    inlines = [TestParticipantsInline, BugInfoInline, BugSurplusInfoInline]


# admin.site.register(TestReport, TestReportAdmin)

# admin.site.register(TestParticipants)
# admin.site.register(BugInfo)
# admin.site.register(BugSurplusInfo)

# class XuegodConfig(AppConfig):
#     name = "xuegod"
#     verbose_name = "测试数据"

# 默认方式
# admin.site.register(TestId)
# admin.site.register()

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'ip', 'phone_status', 'phone_status_select', 'phone_order', 'alter_time')  # 展示的列
    list_display_links = ('name', 'phone', 'ip', 'phone_status', 'phone_status_select', 'phone_order')  # 可以点击的链接
    list_filter = ['name', 'ip']  # 过滤
    search_fields = ['phone', 'ip']  # 搜索


admin.site.register(Resume, ResumeAdmin)


def make_homepage_url_status_on(modeladmin, request, queryset):
    queryset.update(url_status="1")


def make_homepage_url_status_off(modeladmin, request, queryset):
    queryset.update(url_status="0")


make_homepage_url_status_on.short_description = "批量置为显示 "
make_homepage_url_status_off.short_description = "批量置为隐藏 "


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_name', 'url', 'url_status', 'url_type', 'url_order', 'create_time')  # 展示的列
    list_display_links = ('id', 'url_name', 'url', 'url_status', 'url_type', 'url_order')  # 可以点击的链接
    list_filter = ['url_status', 'url_type']  # 过滤
    search_fields = ['url_name']  # 搜索
    actions = [make_homepage_url_status_on, make_homepage_url_status_off]  # 批量操作


admin.site.register(HomePage, HomePageAdmin)
