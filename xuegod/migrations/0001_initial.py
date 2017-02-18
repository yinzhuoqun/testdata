# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_block', models.IntegerField(default=0, verbose_name='紧急')),
                ('bug_major', models.IntegerField(default=0, verbose_name='高')),
                ('bug_normal', models.IntegerField(default=0, verbose_name='中')),
                ('bug_trivial', models.IntegerField(default=0, verbose_name='低')),
            ],
        ),
        migrations.CreateModel(
            name='BugSurplusInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_surplus_block', models.IntegerField(default=0, verbose_name='紧急')),
                ('bug_surplus_major', models.IntegerField(default=0, verbose_name='高')),
                ('bug_surplus_normal', models.IntegerField(default=0, verbose_name='中')),
                ('bug_surplus_trivial', models.IntegerField(default=0, verbose_name='低')),
            ],
        ),
        migrations.CreateModel(
            name='TestId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='账号')),
                ('user_password', models.CharField(max_length=16, verbose_name='密码')),
                ('user_note', models.CharField(blank=True, max_length=32, null=True, verbose_name='备注')),
                ('user_flag', models.CharField(max_length=16, default='0', verbose_name='网络标识')),
                ('user_data_joined', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '测试账号',
                'verbose_name': '账号',
            },
        ),
        migrations.CreateModel(
            name='TestParticipants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_participant', models.CharField(max_length=128, verbose_name='参与人员')),
            ],
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=32, verbose_name='项目名称')),
                ('test_version', models.CharField(max_length=32, verbose_name='测试版本')),
                ('test_platform', models.CharField(default='Android', max_length=32, choices=[('1', 'Android'), ('2', 'iOS'), ('0', 'other')], verbose_name='测试平台')),
                ('test_report_create_time', models.DateTimeField(auto_now_add=True, verbose_name='制表日期')),
                ('test_points', models.TextField(max_length=256, verbose_name='测试要点', help_text='每行一条内容')),
                ('test_cases', models.CharField(max_length=128, verbose_name='测试用例')),
                ('test_way', models.CharField(max_length=32, default='黑盒测试', verbose_name='测试方法')),
                ('test_docs', models.TextField(max_length=256, verbose_name='参考文档', help_text='每行一条内容')),
                ('test_start_time', models.DateTimeField(verbose_name='提测时间')),
                ('test_end_time', models.DateTimeField(verbose_name='结束测试时间')),
                ('test_risks', models.TextField(max_length=256, verbose_name='测试风险', help_text='每行一条内容')),
                ('test_conclusion', models.CharField(max_length=256, verbose_name='测试结论和建议')),
            ],
            options={
                'verbose_name_plural': '测试报告列表',
                'verbose_name': '测试报告',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=14)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='testparticipants',
            name='test_participants',
            field=models.ForeignKey(to='xuegod.TestReport'),
        ),
        migrations.AlterUniqueTogether(
            name='testid',
            unique_together=set([('user_id', 'user_password')]),
        ),
        migrations.AddField(
            model_name='bugsurplusinfo',
            name='bug_surplus_info',
            field=models.ForeignKey(to='xuegod.TestReport'),
        ),
        migrations.AddField(
            model_name='buginfo',
            name='bug_info',
            field=models.ForeignKey(to='xuegod.TestReport'),
        ),
    ]
