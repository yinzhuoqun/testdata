# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0010_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='add_time',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='alter_time',
        ),
    ]
