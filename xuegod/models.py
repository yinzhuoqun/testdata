# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=14) # 字符串
    age = models.IntegerField() #整形
    password = models.CharField(max_length=16)


class TestId(models.Model):
    user_id = models.IntegerField(verbose_name="账号")  # 整形
    user_password = models.CharField(max_length=16, verbose_name="密码")
    # user_note = models.CharField(blank=True, max_length=32)  # 选填
    user_note = models.CharField(null=True, blank=True, max_length=32, verbose_name="备注")
    # blank=True 选填, null=True 为空时 为null

    user_flag = models.CharField(max_length=16, default="0",verbose_name="网络标识")
    user_data_joined = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")


    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "账号"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "测试账号"

        # 是设置某几个字段 联合起来在表中唯一
        unique_together = (("user_id", "user_password"),)



    def __str__(self):
         return "%s|%s|%s"%(self.user_id,self.user_password,self.user_note)

class BugInfo(models.Model):
    # test_version = models.CharField(max_length=32, verbose_name="测试版本")
    # test_platform = models.CharField(max_length=32, default="Android", verbose_name="测试平台")

    bug_block = models.IntegerField(default=0, verbose_name="紧急")
    bug_major = models.IntegerField(default=0, verbose_name="高")
    bug_normal = models.IntegerField(default=0, verbose_name="中")
    bug_trivial = models.IntegerField(default=0, verbose_name="低")

    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "Bug 统计"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "Bug 统计列表"

        # app_label = "测试报告"

    # def __str__(self):
    #     return "%s %s" % (self.test_platform, self.test_version)

class BugSurplusInfo(models.Model):
    # test_version = models.CharField(max_length=32, verbose_name="测试版本")
    # test_platform = models.CharField(max_length=32, default="Android", verbose_name="测试平台")

    bug_surplus_block = models.IntegerField(default=0, verbose_name="紧急")
    bug_surplus_major = models.IntegerField(default=0, verbose_name="高")
    bug_surplus_normal = models.IntegerField(default=0, verbose_name="中")
    bug_surplus_trivial = models.IntegerField(default=0, verbose_name="低")

    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "遗留 Bug 统计"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "遗留 Bug 统计列表"

        # app_label = "测试报告"

    # def __str__(self):
    #     return "%s %s" % (self.test_platform, self.test_version)

class TestParticipants(models.Model):
    # test_version = models.CharField(max_length=32, verbose_name="测试版本")
    # test_platform = models.CharField(max_length=32, default="Android", verbose_name="测试平台")
    test_participant1 = models.CharField(max_length=128, verbose_name="参与人员1")
    test_participant2 = models.CharField(max_length=128, blank=True, verbose_name="参与人员2")
    test_participant3 = models.CharField(max_length=128, blank=True, verbose_name="参与人员3")
    test_participant4 = models.CharField(max_length=128, blank=True, verbose_name="参与人员4")
    test_participant5 = models.CharField(max_length=128, blank=True, verbose_name="参与人员5")
    test_participant6 = models.CharField(max_length=128, blank=True, verbose_name="参与人员6")

    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "测试参与人员"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "测试参与人员列表"

        # app_label = "测试报告"

    # def __str__(self):
    #     return "%s %s" % (self.test_platform, self.test_version)


class TestReport(models.Model):
    input_text = "每行一条内容"

    project_name = models.CharField(max_length=32, verbose_name="项目名称")
    test_version = models.CharField(max_length=32, verbose_name="测试版本")
    test_platform = models.CharField(max_length=32, default="Android", verbose_name="测试平台")
    test_report_create_time = models.DateTimeField(auto_now_add=True, verbose_name="制表日期")
    test_points = models.TextField(max_length=256, help_text=input_text, verbose_name="测试要点")
    # test_points2 = models.TextField(max_length=256, blank=True, help_text=input_text, verbose_name="测试要点2")
    test_cases = models.CharField(max_length=128, verbose_name="测试用例")
    test_way = models.CharField(max_length=32, default="黑盒测试", verbose_name="测试方法")
    test_docs = models.TextField(max_length=256,  help_text=input_text, verbose_name="参考文档")
    test_start_time = models.DateTimeField(verbose_name='提测时间')
    test_end_time = models.DateTimeField(verbose_name='结束测试时间')

    test_participants = models.ForeignKey(TestParticipants)  # 参与人员
    bug_info = models.ForeignKey(BugInfo)  # bug
    bug_surplus = models.ForeignKey(BugSurplusInfo)  # 遗留 bug

    # bug_surplus_total = models.IntegerField(verbose_name="遗留")
    # bug_surplus_block = models.IntegerField(verbose_name="紧急")
    # bug_surplus_major = models.IntegerField(verbose_name="高")
    # bug_surplus_normal = models.IntegerField(verbose_name="中")
    # bug_surplus_trivial = models.IntegerField(verbose_name="低")

    test_risks = models.TextField(max_length=256,  help_text=input_text, verbose_name="测试风险")
    test_conclusion = models.CharField(max_length=256, verbose_name="测试结论和建议")

    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "测试报告"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "测试报告列表"

        # 是设置某几个字段 联合起来在表中唯一
        # unique_together = (("user_id", "user_password"),)

        # app_label = "测试报告"


    def __str__(self):
        return "%s %s" % (self.test_platform, self.test_version)

