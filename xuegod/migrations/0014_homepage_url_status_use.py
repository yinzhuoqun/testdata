# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0013_auto_20170622_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='url_status_use',
            field=models.CharField(help_text='钉钉群链接定制', default='OFF', verbose_name='使用状态', choices=[('1', 'ON'), ('0', 'OFF')], max_length=32),
        ),
    ]
