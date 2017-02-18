# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buginfo',
            options={'verbose_name': 'Bug 统计', 'verbose_name_plural': 'Bug 统计列表'},
        ),
        migrations.AlterModelOptions(
            name='bugsurplusinfo',
            options={'verbose_name': '遗留 Bug 统计', 'verbose_name_plural': '遗留 Bug 统计列表'},
        ),
        migrations.AlterModelOptions(
            name='testparticipants',
            options={'verbose_name': '测试参与人员', 'verbose_name_plural': '测试参与人员列表'},
        ),
        migrations.AlterModelOptions(
            name='testreport',
            options={'verbose_name': '测试报告_V0.9', 'verbose_name_plural': '测试报告列表_V0.9'},
        ),
        migrations.AddField(
            model_name='buginfo',
            name='test_platform',
            field=models.CharField(max_length=32, verbose_name='测试平台', default='Android'),
        ),
        migrations.AddField(
            model_name='buginfo',
            name='test_version',
            field=models.CharField(max_length=32, verbose_name='测试版本', default='1.0.0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bugsurplusinfo',
            name='test_platform',
            field=models.CharField(max_length=32, verbose_name='测试平台', default='Android'),
        ),
        migrations.AddField(
            model_name='bugsurplusinfo',
            name='test_version',
            field=models.CharField(max_length=32, verbose_name='测试版本', default='1.0.0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testparticipants',
            name='test_platform',
            field=models.CharField(max_length=32, verbose_name='测试平台', default='Android'),
        ),
        migrations.AddField(
            model_name='testparticipants',
            name='test_version',
            field=models.CharField(max_length=32, verbose_name='测试版本', default='1.0.0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testreport',
            name='test_platform',
            field=models.CharField(max_length=32, verbose_name='测试平台', default='Android'),
        ),
    ]
