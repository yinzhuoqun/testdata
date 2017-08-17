# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0013_auto_20170816_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdevice',
            name='device_machine_code',
            field=models.CharField(max_length=128, blank=True, null=True, verbose_name='机器码', help_text='如有两个MEID，选最上面的'),
        ),
    ]
