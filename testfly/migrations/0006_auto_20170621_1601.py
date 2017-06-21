# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0005_testdevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdevice',
            name='device_platfrom',
            field=models.CharField(choices=[('1', 'Android'), ('2', 'iOS'), ('0', 'other')], verbose_name='系统平台', default='Android', max_length=48),
        ),
        migrations.AlterField(
            model_name='testdevice',
            name='note',
            field=models.CharField(null=True, blank=True, verbose_name='备注', max_length=256),
        ),
    ]
