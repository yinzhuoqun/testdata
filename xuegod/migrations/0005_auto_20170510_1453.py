# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0004_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(max_length=256, verbose_name='网址')),
                ('url_name', models.CharField(max_length=256, verbose_name='网址名称')),
                ('url_type', models.CharField(max_length=32, verbose_name='类型')),
                ('url_status', models.CharField(choices=[('1', 'ON'), ('0', 'OFF')], verbose_name='显示状态', max_length=32, default='ON')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('alter_time', models.DateTimeField(auto_now=True, verbose_name='最近修改时间')),
            ],
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={'verbose_name_plural': '手机号码列表', 'verbose_name': '手机号码'},
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(unique=True, max_length=48, verbose_name='用户名'),
        ),
    ]
