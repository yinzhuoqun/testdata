# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.forms import widgets

# Register your models here.
from django.apps import AppConfig
from xuegod.models import *


# 不修改Django源码让admin中的Model列表按注册顺序显示
from django.contrib import admin
from django.utils.text import capfirst
from django.utils.datastructures import SortedDict


def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        for app in templateresponse.context_data['app_list']:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return templateresponse

    return inner


# RemovedInDjango19Warning: SortedDict is deprecated and will be removed in Django 1.9.
registry = SortedDict()
registry.update(admin.site._registry)
admin.site._registry = registry
admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)

# 不修改Django源码让admin中的Model列表按注册顺序显示

# @admin.register( TestId ) # 注册方法1
class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'alimysql'  # 数据库
    list_display = ('id', 'user_id', 'user_password', 'user_note', 'user_flag')  # 展示列表项
    list_filter = ['user_flag']  # 过滤器
    search_fields = ['user_id']  # 搜索框
    list_display_links = ('id', 'user_id', 'user_password')
    list_max_show_all = 20  # 控制在“显示所有”管理更改列表页面上可以显示的项目数，默认设置为100
    list_per_page = 25  # 控制Admin 修改列表页面每页中显示多少项，默认设置为100。

    # def width_id(self):
    #     return format_html('<span style="width:275px;">{}</span>',
    #                        self.user_id,
    #                        # self.first_name,
    #                        # self.last_name,
    #                        )
    #
    # width_id.allow_tags = True

    # 通过一种临时的方案来覆盖现有的模型中Field （字段）类型在admin site中的显示类型
    # http://python.usyiyi.cn/translate/django_182/ref/contrib/admin/index.html
    formfield_overrides = {
        models.IntegerField: {'widget': widgets.TextInput},
        models.CharField: {'widget': widgets.TextInput},
    }

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        # obj.user = request.user
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


# 指定数据库，注册方法2
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
    def phone_status_on(self, request, queryset):
        queryset.update(phone_status="1")

    def phone_status_off(self, request, queryset):
        queryset.update(phone_status="0")

    phone_status_on.short_description = "批量置为必定使用 "
    phone_status_off.short_description = "批量置为必定不使用 "

    def phone_status_select_on(self, request, queryset):
        queryset.update(phone_status_select="1")

    def phone_status_select_off(self, request, queryset):
        queryset.update(phone_status_select="0")

    phone_status_select_on.short_description = "批量置为上传使用 "
    phone_status_select_off.short_description = "批量置为上传不使用 "

    readonly_fields = []  # 只读字段
    list_display = (
        'id', 'name', 'phone', 'email', 'ip', 'colored_phone_status', 'colored_phone_status_select', 'phone_order', 'note', 'alter_time')  # 展示的列
    list_display_links = (
        'id', 'name', 'phone', 'ip', 'email', 'colored_phone_status', 'colored_phone_status_select', 'note', 'phone_order')  # 可以点击的链接
    list_filter = ['name', 'ip']  # 过滤
    search_fields = ['phone', 'ip']  # 搜索
    actions = [phone_status_off, phone_status_on, phone_status_select_off, phone_status_select_on]


admin.site.register(Resume, ResumeAdmin)


def make_homepage_url_status_on(modeladmin, request, queryset):
    queryset.update(url_status="1")


def make_homepage_url_status_off(modeladmin, request, queryset):
    queryset.update(url_status="0")


make_homepage_url_status_on.short_description = "批量置为显示 "
make_homepage_url_status_off.short_description = "批量置为隐藏 "


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'colored_url_name', 'url_nickname', 'url', 'colored_url_status',
                    'colored_url_status_use', 'url_type', 'url_order',
                    'create_time')  # 展示的列
    list_display_links = (
        'id', 'colored_url_name', 'url_nickname', 'url', 'colored_url_status',
        'colored_url_status_use', 'url_type', 'url_order', 'create_time')  # 可以点击的链接
    list_filter = ['url_status', 'url_type']  # 过滤
    search_fields = ['url_name']  # 搜索
    actions = [make_homepage_url_status_on, make_homepage_url_status_off]  # 批量操作


admin.site.register(HomePage, HomePageAdmin)


class IndexNavInline(admin.StackedInline):
    model = IndexNav  # 模型名称
    extra = 1  # 默认数量


class IndexNavAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'url', 'fullname', 'nickname', 'url_type', 'order', 'show_status', 'create_time')


class IndexTypeAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('url_type',)
    inlines = [IndexNavInline, ]


class IndexTypeAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('id', 'url_type', 'create_time', 'alter_time')


# admin.site.register(IndexType, IndexTypeAdmin)
admin.site.register(IndexType, IndexTypeAdmin)
admin.site.register(IndexNav, IndexNavAdmin)


class VestInfoAdmin(admin.ModelAdmin):
    search_fields = ['owner']
    filter_horizontal = ('id_info',)  # ManyToMany多对多字段编辑更方便，左右形式
    # filter_vertical = ('id_info',)  #  # ManyToMany多对多字段编辑更方便，上下形式
    list_display = list_display_links = ('id','owner', 'position',  'id_infos', 'order', 'show_status', 'create_time')


class VestAccountAdmin(admin.ModelAdmin):
    search_fields = ['account']
    list_display = list_display_links = ('id', 'account', 'gender', 'name', 'alter_time', 'create_time')


class PositionTypeAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('id', 'position_type', 'alter_time', 'create_time')


admin.site.register(PositionType, PositionTypeAdmin)
admin.site.register(VestAccount, VestAccountAdmin)
admin.site.register(VestInfo, VestInfoAdmin)
