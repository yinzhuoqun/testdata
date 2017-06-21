# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0007_auto_20170621_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testdevice',
            options={'verbose_name': '设备借用信息', 'verbose_name_plural': '设备借用信息列表'},
        ),
    ]
