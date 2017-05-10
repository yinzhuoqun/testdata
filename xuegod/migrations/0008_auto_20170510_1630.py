# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0007_auto_20170510_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='url_order',
            field=models.IntegerField(help_text='值越小，同分类中越靠前显示', default=0, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='url_type',
            field=models.CharField(help_text='自定义类型，方便区分', default='other', max_length=32, verbose_name='类型'),
        ),
    ]
