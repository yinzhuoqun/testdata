# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0005_auto_20170510_1453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': '网址信息', 'verbose_name_plural': '网址信息列表'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='url_order',
            field=models.IntegerField(verbose_name='序号', default=0, max_length=32),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='url_status',
            field=models.CharField(verbose_name='显示状态', default='ON', help_text='是否显示到网站', max_length=32, choices=[('1', 'ON'), ('0', 'OFF')]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='url_type',
            field=models.CharField(verbose_name='类型', help_text='自定义类型，方便区分', max_length=32),
        ),
    ]
