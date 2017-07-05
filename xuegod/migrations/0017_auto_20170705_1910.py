# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0016_auto_20170704_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='indextype',
            name='alter_time',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 7, 5, 11, 10, 25, 499236, tzinfo=utc), verbose_name='最近修改时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indextype',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 7, 5, 11, 10, 30, 397714, tzinfo=utc), verbose_name='创建时间'),
            preserve_default=False,
        ),
    ]
