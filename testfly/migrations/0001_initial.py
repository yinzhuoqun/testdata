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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('bug_block', models.IntegerField(verbose_name='紧急', default=0)),
                ('bug_major', models.IntegerField(verbose_name='高', default=0)),
                ('bug_normal', models.IntegerField(verbose_name='中', default=0)),
                ('bug_trivial', models.IntegerField(verbose_name='低', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BugSurplusInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('bug_surplus_block', models.IntegerField(verbose_name='紧急', default=0)),
                ('bug_surplus_major', models.IntegerField(verbose_name='高', default=0)),
                ('bug_surplus_normal', models.IntegerField(verbose_name='中', default=0)),
                ('bug_surplus_trivial', models.IntegerField(verbose_name='低', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TestParticipants',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('test_participant', models.CharField(verbose_name='参与人员', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('project_name', models.CharField(verbose_name='项目名称', max_length=32)),
                ('test_version', models.CharField(verbose_name='测试版本', max_length=32)),
                ('test_platform', models.CharField(verbose_name='测试平台', choices=[('1', 'Android'), ('2', 'iOS'), ('0', 'other')], default='Android', max_length=32)),
                ('test_report_create_time', models.DateTimeField(verbose_name='制表日期', auto_now_add=True)),
                ('test_report_alter_time', models.DateTimeField(verbose_name='最近修改时间', auto_now=True)),
                ('test_points', models.TextField(verbose_name='测试要点', help_text='每行一条内容', max_length=256)),
                ('test_cases', models.CharField(verbose_name='测试用例', max_length=128)),
                ('test_way', models.CharField(verbose_name='测试方法', default='黑盒测试', max_length=32)),
                ('test_docs', models.TextField(verbose_name='参考文档', help_text='每行一条内容', max_length=256)),
                ('test_start_time', models.DateTimeField(verbose_name='提测时间')),
                ('test_end_time', models.DateTimeField(verbose_name='结束测试时间')),
                ('test_risks', models.TextField(verbose_name='测试风险', help_text='每行一条内容', max_length=256)),
                ('test_conclusion', models.CharField(verbose_name='测试结论和建议', max_length=256)),
            ],
            options={
                'verbose_name': '测试报告',
                'verbose_name_plural': '测试报告列表',
            },
        ),
        migrations.AddField(
            model_name='testparticipants',
            name='test_participants',
            field=models.ForeignKey(to='testfly.TestReport'),
        ),
        migrations.AddField(
            model_name='bugsurplusinfo',
            name='bug_surplus_info',
            field=models.ForeignKey(to='testfly.TestReport'),
        ),
        migrations.AddField(
            model_name='buginfo',
            name='bug_info',
            field=models.ForeignKey(to='testfly.TestReport'),
        ),
    ]
