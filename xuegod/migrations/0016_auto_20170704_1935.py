# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0015_auto_20170704_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexnav',
            name='url_type',
            field=models.ForeignKey(to='xuegod.IndexType', related_name='type_set', verbose_name='分类'),
        ),
    ]
