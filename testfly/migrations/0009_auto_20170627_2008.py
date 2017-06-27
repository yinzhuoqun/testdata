# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0008_auto_20170621_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdevice',
            name='add_time',
            field=models.DateTimeField(verbose_name='添加日期', default=datetime.datetime(2017, 6, 27, 12, 8, 38, 522119, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testdevice',
            name='device_machine_code',
            field=models.CharField(max_length=128, help_text='如有两个MEID，选最上面的', null=True, verbose_name='机器码', blank=True),
        ),
        migrations.AlterField(
            model_name='testdevice',
            name='alter_time',
            field=models.DateTimeField(auto_now=True, verbose_name='变更日期'),
        ),
        migrations.AlterField(
            model_name='testdevice',
            name='use_time',
            field=models.DateTimeField(verbose_name='领用日期', null=True, blank=True),
        ),
    ]
