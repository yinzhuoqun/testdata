# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0003_auto_20170405_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=48, unique=True, verbose_name='姓名')),
                ('phone', models.CharField(max_length=32, verbose_name='手机')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('alter_time', models.DateTimeField(verbose_name='最近修改时间', auto_now=True)),
            ],
        ),
    ]
