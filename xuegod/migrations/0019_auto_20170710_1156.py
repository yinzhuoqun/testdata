# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0018_auto_20170710_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vestaccount',
            options={'verbose_name_plural': '马甲账号列表', 'verbose_name': '马甲账号'},
        ),
        migrations.AlterModelOptions(
            name='vestinfo',
            options={'verbose_name_plural': '马甲账号信息列表', 'verbose_name': '马甲账号信息'},
        ),
    ]
