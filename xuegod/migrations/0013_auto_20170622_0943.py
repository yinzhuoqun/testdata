# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0012_auto_20170619_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='url_nickname',
            field=models.CharField(verbose_name='简短名称', max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='url_name',
            field=models.CharField(verbose_name='显示名称', max_length=256),
        ),
    ]
