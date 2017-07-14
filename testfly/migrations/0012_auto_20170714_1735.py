# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0011_auto_20170714_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 9, 35, 50, 647390, tzinfo=utc), auto_now_add=True, verbose_name='添加日期'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='alter_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 9, 35, 53, 720563, tzinfo=utc), auto_now=True, verbose_name='变更日期'),
            preserve_default=False,
        ),
    ]
