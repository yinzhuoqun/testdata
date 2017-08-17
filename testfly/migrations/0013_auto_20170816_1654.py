# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0012_auto_20170714_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdevice',
            name='device_machine_code',
            field=models.CharField(null=True, default=None, max_length=128, verbose_name='机器码', help_text='如有两个MEID，选最上面的', blank=True),
        ),
    ]
