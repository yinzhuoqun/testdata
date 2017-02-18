# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testparticipants',
            name='test_participant',
            field=models.CharField(verbose_name='参与测试人员', max_length=128),
        ),
        migrations.AlterField(
            model_name='testreport',
            name='test_docs',
            field=models.TextField(verbose_name='参考文档', null=True, help_text='每行一条内容, HTML展示时序号会自动添加', max_length=256, blank=True),
        ),
        migrations.AlterField(
            model_name='testreport',
            name='test_points',
            field=models.TextField(verbose_name='测试要点', help_text='每行一条内容, HTML展示时序号会自动添加', max_length=256),
        ),
        migrations.AlterField(
            model_name='testreport',
            name='test_risks',
            field=models.TextField(verbose_name='测试风险', null=True, help_text='每行一条内容, HTML展示时序号会自动添加', max_length=256, blank=True),
        ),
    ]
