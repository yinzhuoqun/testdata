# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0021_auto_20170710_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positiontype',
            name='position_type',
            field=models.CharField(verbose_name='职位名称', max_length=128),
        ),
        migrations.AlterField(
            model_name='vestinfo',
            name='position',
            field=models.ForeignKey(null=True, blank=True, related_name='position_set', verbose_name='职位昵称', to='xuegod.PositionType'),
        ),
    ]
