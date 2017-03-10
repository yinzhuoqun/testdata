from django.contrib import admin

# Register your models here.


from testfly.models import *


class TestParticipantsInline(admin.TabularInline):
    model = TestParticipants  # 模型名称
    extra = 3  # 默认数量


class BugSurplusInfoInline(admin.TabularInline):
    model = BugSurplusInfo
    extra = 1  # 默认数量


class BugInfoInline(admin.TabularInline):
    model = BugInfo
    extra = 1  # 默认数量


class TestReportAdmin(admin.ModelAdmin):
    list_display = ('project_name',  'test_platform', 'test_version')  # 单元素元组要加逗号
    list_filter = ['test_platform']  # 过滤
    search_fields = ['test_version']
    # fieldsets = [
    #     ("BUG 信息", {'fields': [""]}),
    #     ("参与人员", {'fields:['']'})
    # ]
    #
    inlines = [TestParticipantsInline, BugInfoInline, BugSurplusInfoInline]


admin.site.register(TestReport, TestReportAdmin)
