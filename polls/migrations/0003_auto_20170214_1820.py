# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170214_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='quesiton',
            new_name='question',
        ),
    ]
