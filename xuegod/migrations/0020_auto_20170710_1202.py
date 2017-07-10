# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0019_auto_20170710_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vestaccount',
            name='gender',
            field=models.CharField(max_length=32, verbose_name='账号性别', default='男', choices=[('1', '男'), ('0', '女')]),
        ),
    ]
