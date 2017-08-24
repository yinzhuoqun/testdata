# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0024_resume_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(max_length=128, verbose_name='邮箱', blank=True, null=True),
        ),
    ]
