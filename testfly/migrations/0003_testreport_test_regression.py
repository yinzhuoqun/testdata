# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0002_auto_20170216_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='testreport',
            name='test_regression',
            field=models.CharField(default='/', max_length=128, verbose_name='回归情况'),
            preserve_default=False,
        ),
    ]
