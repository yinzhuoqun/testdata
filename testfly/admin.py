from django.contrib import admin

# Register your models here.


from testfly.models import *


class TestParticipantsInline(admin.TabularInline):
    model = TestParticipants  # 模型名称
    extra = 3  # 默认数量


class BugSurplusInfoInline(admin.TabularInline):
    model = BugSurplusInfo  # 模型名称
    extra = 1  # 默认数量
    max_num = 1  # 最大数量


class BugInfoInline(admin.TabularInline):
    model = BugInfo  # 模型名称
    extra = 1  # 默认数量
    max_num = 1  # 最大数量


class TestReportAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'test_platform', 'test_version')  # 单元素元组要加逗号
    # list_display = ('__str__',  'test_platform', 'test_version')  # 单元素元组要加逗号
    # list_display_links = ('__str__', 'test_platform', 'test_version')  # 可以控制list_display中的字段是否应该链接到对象的“更改”页面
    list_display_links = ('project_name', 'test_platform', 'test_version')  # 可以控制list_display中的字段是否应该链接到对象的“更改”页面
    # list_display_links = None  # 更改列表页面网格将没有链接
    list_filter = ['project_name', 'test_platform', 'test_version']  # 过滤
    search_fields = ['test_version']
    save_on_top = True
    # fieldsets = [
    #     ("BUG 信息", {'fields': [""]}),
    #     ("参与人员", {'fields:['']'})
    # ]
    #
    inlines = [TestParticipantsInline, BugInfoInline, BugSurplusInfoInline]


admin.site.register(TestReport, TestReportAdmin)


class TestDeviceAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        "id", "device_order", "device_name", "device_screen_size", "device_screen_resolution",
        "device_platfrom", "device_platfrom_version", "device_machine_code", "use_name", "use_time", "return_time",
        "alter_time", "note", "device_show_status",
    )
    list_filter = ["device_platfrom", "device_platfrom_version", "use_name"]  # 过滤
    search_fields = ["use_name", "device_name"]

admin.site.register(TestDevice, TestDeviceAdmin)