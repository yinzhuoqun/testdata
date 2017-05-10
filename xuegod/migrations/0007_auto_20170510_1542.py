# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0006_auto_20170510_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='url_order',
            field=models.IntegerField(default=0, verbose_name='序号'),
        ),
    ]
