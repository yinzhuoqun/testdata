# -*- coding: utf-8 -*-
from django.db import models
from django.utils.html import format_html  # Django 将默认转义HTML输出
# from django import forms


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=14)  # 字符串
    age = models.IntegerField()  # 整形
    password = models.CharField(max_length=16)


class TestId(models.Model):
    user_flag_choice = (
        ("1", "外网"),
        ('0', '内网'),
    )

    user_id = models.IntegerField(unique=True, verbose_name="账号")  # 整形
    user_password = models.CharField(max_length=16, verbose_name="密码")
    # user_note = models.CharField(blank=True, max_length=32)  # 选填
    user_note = models.CharField(null=True, blank=True, max_length=32, verbose_name="备注")
    # blank=True 选填, null=True 为空时 为null

    user_flag = models.CharField(max_length=16, default="0", choices=user_flag_choice, verbose_name="网络标识",
                                 help_text="内网是 0，外网是 1")
    user_data_joined = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "账号账号"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "测试账号列表"

        # 是设置某几个字段 联合起来在表中唯一
        unique_together = (("user_id", "user_password"),)

    def __str__(self):
        return "%s|%s" % (self.user_id, self.user_password)


class TestReport(models.Model):
    input_text = "每行一条内容"
    # test_platform_choice = (
    #     ("1", "Android"),
    #     ('2', 'iOS'),
    #     ('0', 'other'),
    # )

    project_name = models.CharField(max_length=32, verbose_name="项目名称")
    test_version = models.CharField(max_length=32, verbose_name="测试版本")
    # test_platform = models.CharField(max_length=32, choices=test_platform_choice, default="Android", verbose_name="测试平台")
    test_platform = models.CharField(max_length=32, default="Android", verbose_name="测试平台")
    test_report_create_time = models.DateTimeField(auto_now_add=True, verbose_name="制表日期")
    test_points = models.TextField(max_length=256, help_text=input_text, verbose_name="测试要点")
    test_cases = models.CharField(max_length=128, verbose_name="测试用例")
    test_way = models.CharField(max_length=32, default="黑盒测试", verbose_name="测试方法")
    test_docs = models.TextField(max_length=256, help_text=input_text, verbose_name="参考文档")
    test_start_time = models.DateTimeField(verbose_name='提测时间')
    test_end_time = models.DateTimeField(verbose_name='结束测试时间')

    test_risks = models.TextField(max_length=256, help_text=input_text, verbose_name="测试风险")
    test_conclusion = models.CharField(max_length=256, verbose_name="测试结论和建议")

    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "测试报告_V0.9"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "测试报告列表_V0.9"

        # 是设置某几个字段 联合起来在表中唯一
        # unique_together = (("user_id", "user_password"),)

        # app_label = "测试报告"

    def __str__(self):
        return "%s %s" % (self.test_platform, self.test_version)


class BugInfo(models.Model):
    test_version = models.CharField(max_length=32, verbose_name="测试版本")
    test_platform = models.CharField(max_length=32, default="Android", verbose_name="测试平台")
    bug_info = models.ForeignKey(TestReport)
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

    def __str__(self):
        return "%s %s" % (self.test_platform, self.test_version)


class BugSurplusInfo(models.Model):
    test_version = models.CharField(max_length=32, verbose_name="测试版本")
    test_platform = models.CharField(max_length=32, default="Android", verbose_name="测试平台")
    bug_surplus_info = models.ForeignKey(TestReport)
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

    def __str__(self):
        return "%s %s" % (self.test_platform, self.test_version)


class TestParticipants(models.Model):
    test_version = models.CharField(max_length=32, verbose_name="测试版本")
    test_platform = models.CharField(max_length=32, default="Android", verbose_name="测试平台")
    test_participants = models.ForeignKey(TestReport)
    test_participant = models.CharField(max_length=128, verbose_name="参与人员")

    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "测试参与人员"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "测试参与人员列表"

    # # app_label = "测试报告"
    # 从Django1.7以后不再使用app_label，修改app相关需要使用AppConfig

    def __str__(self):
        return self.test_participant


class Resume(models.Model):
    phone_status_choice = (
        ("1", "ON"),
        ('0', 'OFF'),
    )

    name = models.CharField(unique=True, max_length=48, verbose_name="用户名称")
    phone = models.CharField(max_length=32, verbose_name="手机号码")
    email = models.EmailField(max_length=128, null=True, blank=True, verbose_name="邮箱")
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP")
    phone_order = models.IntegerField(default=0, verbose_name="序号", help_text="值越小，同分类中越靠前显示")
    phone_status = models.CharField(max_length=32, choices=phone_status_choice, default="0FF", verbose_name="必定使用",
                                    help_text="一定使用该号码")
    phone_status_select = models.CharField(max_length=32, choices=phone_status_choice, default="ON",
                                           verbose_name="上传使用",
                                           help_text="上传文件时，IP 在范围之内才使用")
    note = models.CharField(max_length=256, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    alter_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')

    class Meta:
        # meta 是否固定？
        # 设置的是后台显示表名  默认是类名
        verbose_name = "手机号码"

        # 是设置复数形式时显示的名称
        verbose_name_plural = "手机号码列表"

    def __str__(self):
        return "%s" % self.name

    def colored_phone_status(self):
        return self.phone_status == "ON" or self.phone_status == "1"
    colored_phone_status.boolean = True
    colored_phone_status.short_description = "必定使用"

    def colored_phone_status_select(self):
        return self.phone_status_select == "ON" or self.phone_status_select == "1"

    colored_phone_status_select.boolean = True
    colored_phone_status_select.short_description = "上传使用"



class HomePage(models.Model):
    url_status_choice = (
        ("1", "ON"),
        ('0', 'OFF'),
    )

    url = models.CharField(max_length=256, verbose_name="网址")
    url_name = models.CharField(max_length=256, verbose_name="显示名称")
    url_nickname = models.CharField(max_length=256, blank=True, null=True, verbose_name="简短名称")
    url_type = models.CharField(max_length=32, default="other", verbose_name="类型", help_text="自定义类型，方便区分")
    url_order = models.IntegerField(default=0, verbose_name="序号", help_text="值越小，同分类中越靠前显示")
    url_status = models.CharField(max_length=32, choices=url_status_choice, default="ON", verbose_name="显示状态",
                                  help_text="是否显示到网站")
    url_status_use = models.CharField(max_length=32, choices=url_status_choice, default="OFF", verbose_name="使用状态",
                                      help_text="钉钉群链接定制")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    alter_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')

    def colored_url_status(self):
        # if self.url_status == "ON" or self.url_status == "1":
        #     color_code = "green"
        # else:
        #     color_code = "red"
        # return format_html('<span style="color:{};">{}</span>',
        #                    color_code,
        #                    self.url_status)

        return self.url_status == 'ON' or self.url_status == '1'

    colored_url_status.boolean = True  # 变成布尔值
    # Django 将默认转义HTML输出。如果你不希望转义方法的输出，可以给方法一个allow_tags 属性，其值为True。
    colored_url_status.allow_tags = True
    # colored_url_status.admin_order_field = 'url_status'  # 在Admin 中按照按colored_first_name 排序时依据first_name 字段
    colored_url_status.short_description = "网页显示状态"  # 新字段的显示的名称

    def colored_url_name(self):
        if self.url_status == "ON" or self.url_status == "1":
            color_code = "green"
        else:
            color_code = "red"
        return format_html('<span style="color:{}">{}</span>',
                           color_code,
                           self.url_name
                           )
    colored_url_name.short_description = "显示名称"  # 新字段的显示的名称

    def colored_url_status_use(self):
        return self.url_status_use == "1"
    colored_url_status_use.boolean = True
    colored_url_status_use.short_description = "钉钉使用状态"

    def __str__(self):
        return "%s" % self.url_name

    class Meta:
        verbose_name = "网址信息"
        verbose_name_plural = "网址信息列表"


class IndexType(models.Model):
    url_type = models.CharField(max_length=32, default="other", verbose_name="类型", help_text="自定义类型，方便区分")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    alter_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')

    class Meta:
        verbose_name = "导航类型"
        verbose_name_plural = "导航类型列表"

    def __str__(self):
        return "%s" % self.url_type


class IndexNav(models.Model):
    status_choice = (
        ("1", "ON"),
        ('0', 'OFF'),
    )

    url = models.CharField(max_length=256, verbose_name="网址")
    fullname = models.CharField(max_length=256, verbose_name="显示名称")
    nickname = models.CharField(max_length=256, blank=True, null=True, verbose_name="简短名称")
    url_type = models.ForeignKey('IndexType', related_name='type_set', verbose_name="分类")
    order = models.IntegerField(default=0, verbose_name="序号", help_text="值越小，同分类中越靠前显示")
    show_status = models.BooleanField(max_length=32, default=True, verbose_name="显示状态",
                                      help_text="是否显示到网站")
    # select_status = models.BooleanField(max_length=32, default=False, verbose_name="选择使用",
    #                                  help_text="钉钉群链接定制")
    # use_status = models.BooleanField(max_length=32, default=False, verbose_name="必定使用",
    #                               help_text="钉钉群链接定制")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    alter_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')

    class Meta:
        verbose_name = "导航网址"
        verbose_name_plural = "导航网址列表"

    def __str__(self):
        return "%s" % self.fullname

class PositionType(models.Model):
    position_type = models.CharField(max_length=128, verbose_name="职位名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    alter_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')

    class Meta:
        verbose_name = "职位名称"
        verbose_name_plural = "职位名称列表"

    def __str__(self):
        return "%s" % self.position_type


class VestAccount(models.Model):
    gender_choice = (
        ("1", "男"),
        ('0', "女"),
    )
    account = models.CharField(unique=True, max_length=32, verbose_name="账号")
    gender = models.CharField(max_length=32, choices=gender_choice, default="男", verbose_name="账号性别")
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name="账号昵称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    alter_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')

    class Meta:
        verbose_name = "马甲账号"
        verbose_name_plural = "马甲账号列表"
        ordering = ['-gender']  # 反向排序

    def __str__(self):
        if self.gender == "1":
            self.gender = "男"
        else:
            self.gender = "女"
        return "%s %s %s" % (self.account, self.gender, self.name)

class VestInfo(models.Model):
    owner = models.CharField(max_length=128, verbose_name="姓名")
    # position = models.CharField(max_length=128, blank=True, null=True, verbose_name="职位")
    position = models.ForeignKey("PositionType", related_name="position_set", verbose_name="职位昵称")
    id_info = models.ManyToManyField('VestAccount', related_name='id_set', verbose_name="账号信息", help_text="1 是男性，0 是女性")
    order = models.IntegerField(default=0, verbose_name="序号", help_text="值越小，同分类中越靠前显示")
    show_status = models.BooleanField(max_length=32, default=True, verbose_name="显示状态",
                                      help_text="是否显示到网站")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    alter_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')

    class Meta:
        verbose_name = "马甲账号信息"
        verbose_name_plural = "马甲账号信息列表"

    def __str__(self):
        return "%s" % self.owner

    def id_infos(self):
        vestinfo = VestInfo.objects.get(id=self.pk)
        accountinfos = ""
        for accountinfo in vestinfo.id_info.filter():
            accountinfos += str(accountinfo) + "；"
        return accountinfos
    id_infos.short_description = "马甲账号"
