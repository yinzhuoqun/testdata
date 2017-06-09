# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0009_auto_20170609_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='phone_order',
            field=models.IntegerField(help_text='值越小，同分类中越靠前显示', verbose_name='序号', default=0),
        ),
        migrations.AddField(
            model_name='resume',
            name='phone_status',
            field=models.CharField(max_length=32, choices=[('1', 'ON'), ('0', 'OFF')], help_text='是否使用该号码', verbose_name='使用状态', default='ON'),
        ),
    ]
