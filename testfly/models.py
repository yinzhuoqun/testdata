from django.db import models


# Create your models here.


class TestReport(models.Model):
    input_text = "每行一条内容, HTML展示时序号会自动添加"
    test_platform_choice = (
        ("1", "Android"),
        ('2', 'iOS'),
        ('0', 'other'),
    )

    project_name = models.CharField(max_length=32, verbose_name="项目名称")
    test_version = models.CharField(max_length=32, verbose_name="测试版本")
    test_platform = models.CharField(max_length=32, choices=test_platform_choice, default="Android",
                                     verbose_name="测试平台")
    test_report_create_time = models.DateTimeField(auto_now_add=True, verbose_name="制表日期")
    test_report_alter_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    test_points = models.TextField(max_length=256, help_text=input_text, verbose_name="测试要点")
    test_cases = models.CharField(max_length=128, verbose_name="测试用例")
    test_regression = models.CharField(max_length=128, verbose_name="回归情况")
    test_way = models.CharField(max_length=32, default="黑盒测试", verbose_name="测试方法")
    test_docs = models.TextField(max_length=256, blank=True, null=True, help_text=input_text, verbose_name="参考文档")
    test_start_time = models.DateTimeField(verbose_name='提测时间')
    test_end_time = models.DateTimeField(verbose_name='结束测试时间')

    test_risks = models.TextField(max_length=256, blank=True, null=True, help_text=input_text, verbose_name="测试风险")
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
        #
        # def __str__(self):
        #     if self.test_platform == "1":
        #         self.test_platform = "Android"
        #     elif self.test_platform == "2":
        #         self.test_platform = "iOS"
        #     else:
        #         self.test_platform = "other"
        #
        #     return "%s %s_v%s" % (self.project_name, self.test_platform, self.test_version)


class BugInfo(models.Model):
    bug_info = models.ForeignKey(TestReport)  # 外键到 TestReport
    bug_block = models.IntegerField(default=0, verbose_name="紧急")
    bug_major = models.IntegerField(default=0, verbose_name="高")
    bug_normal = models.IntegerField(default=0, verbose_name="中")
    bug_trivial = models.IntegerField(default=0, verbose_name="低")

    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "提交 Bug 统计"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "提交 Bug 统计列表"

        # app_label = "测试报告"

        # def __str__(self):
        #     return "%s %s" % (self.test_platform, self.test_version)


class BugSurplusInfo(models.Model):
    bug_surplus_info = models.ForeignKey(TestReport)  # 外键到 TestReport
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
    test_participants = models.ForeignKey(TestReport)  # 外键到 TestReport
    test_participant = models.CharField(max_length=128, verbose_name="参与测试人员")

    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "测试参与人员"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "测试参与人员列表"

    #
    #     # app_label = "测试报告"

    def __str__(self):
        return self.test_participant


class TestDevice(models.Model):
    device_platfrom_choice = (
        ("1", "Android"),
        ('2', 'iOS'),
        ('0', 'other'),
    )

    device_show_status_choice = (
        ("1", "显示"),
        ("0", "隐藏")
    )

    device_order = models.IntegerField(default=0, verbose_name="序号", help_text="值越小，同分类中越靠前显示")
    device_name = models.CharField(max_length=128, verbose_name="设备名称", help_text="设备的中文名称")
    device_screen_size = models.CharField(max_length=48, blank=True, null=True, verbose_name="屏幕尺寸",
                                          help_text="单位：英寸，如：5.5")
    device_screen_resolution = models.CharField(max_length=48, blank=True, null=True, verbose_name="分辨率",
                                                help_text="单位：像素，如：1920*1080")
    device_platfrom = models.CharField(max_length=48, choices=device_platfrom_choice, default="Android",
                                       verbose_name="系统平台")
    device_platfrom_version = models.CharField(max_length=48, blank=True, null=True, verbose_name="系统版本",
                                               help_text="如：4.3")
    device_machine_code = models.CharField(max_length=128, blank=True, null=True, verbose_name="机器码",
                                           help_text="如有两个MEID，选最上面的")
    use_name = models.CharField(max_length=128, blank=True, null=True, verbose_name="领用人员",
                                help_text="如：张三")
    use_time = models.DateTimeField(blank=True, null=True, verbose_name='领用日期')
    return_time = models.DateTimeField(blank=True, null=True, verbose_name='归还日期')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加日期")
    alter_time = models.DateTimeField(auto_now=True, verbose_name='变更日期')
    device_show_status = models.CharField(max_length=48, choices=device_show_status_choice, default="显示",
                                          verbose_name="是否显示到网页")
    note = models.CharField(max_length=256, blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "设备借用信息"
        verbose_name_plural = "设备借用信息列表"

    def __str__(self):
        return "%s|%s" % (self.use_name, self.device_name)


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=48)
    content = models.TextField(max_length=256)
    author = models.CharField(max_length=48)
    source = models.CharField(max_length=48)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加日期")
    alter_time = models.DateTimeField(auto_now=True, verbose_name='变更日期')
