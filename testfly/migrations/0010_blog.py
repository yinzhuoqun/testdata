# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0009_auto_20170627_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=48)),
                ('content', models.TextField(max_length=256)),
                ('author', models.CharField(max_length=48)),
                ('source', models.CharField(max_length=48)),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加日期')),
                ('alter_time', models.DateTimeField(auto_now=True, verbose_name='变更日期')),
            ],
        ),
    ]
