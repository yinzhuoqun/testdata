# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0010_auto_20170609_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='phone_status_select',
            field=models.CharField(verbose_name='使用状态', choices=[('1', 'ON'), ('0', 'OFF')], help_text='IP 在范围之内才使用', max_length=32, default='ON'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone_status',
            field=models.CharField(verbose_name='必定使用', choices=[('1', 'ON'), ('0', 'OFF')], help_text='一定使用该号码', max_length=32, default='0FF'),
        ),
    ]
