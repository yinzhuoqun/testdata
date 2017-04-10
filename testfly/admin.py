from django.contrib import admin

# Register your models here.


from testfly.models import *


class TestParticipantsInline(admin.TabularInline):
    model = TestParticipants  # 模型名称
    extra = 3  # 默认数量


class BugSurplusInfoInline(admin.TabularInline):
    model = BugSurplusInfo
    extra = 1  # 默认数量
    max_num = 1


class BugInfoInline(admin.TabularInline):
    model = BugInfo
    extra = 1  # 默认数量
    max_num = 1


class TestReportAdmin(admin.ModelAdmin):
    list_display = ('project_name',  'test_platform', 'test_version')  # 单元素元组要加逗号
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
