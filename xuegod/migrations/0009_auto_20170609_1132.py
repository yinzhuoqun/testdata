# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0008_auto_20170510_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(unique=True, max_length=48, verbose_name='用户名称'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(max_length=32, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='testid',
            name='user_flag',
            field=models.CharField(default='0', max_length=16, help_text='内网是 0，外网是 1', choices=[('1', '外网'), ('0', '内网')], verbose_name='网络标识'),
        ),
    ]
