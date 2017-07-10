# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0022_auto_20170710_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vestaccount',
            options={'ordering': ['-gender'], 'verbose_name_plural': '马甲账号列表', 'verbose_name': '马甲账号'},
        ),
        migrations.AlterField(
            model_name='vestinfo',
            name='position',
            field=models.ForeignKey(to='xuegod.PositionType', related_name='position_set', default=datetime.datetime(2017, 7, 10, 14, 25, 21, 100563, tzinfo=utc), verbose_name='职位昵称'),
            preserve_default=False,
        ),
    ]
