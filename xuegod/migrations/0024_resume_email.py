# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0023_auto_20170710_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='email',
            field=models.CharField(max_length=128, blank=True, null=True, verbose_name='邮箱'),
        ),
    ]
