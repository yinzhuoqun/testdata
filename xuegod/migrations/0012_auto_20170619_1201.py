# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0011_auto_20170609_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='note',
            field=models.CharField(max_length=256, verbose_name='备注', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone_status_select',
            field=models.CharField(max_length=32, default='ON', verbose_name='上传使用', help_text='上传文件时，IP 在范围之内才使用', choices=[('1', 'ON'), ('0', 'OFF')]),
        ),
    ]
