# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0017_auto_20170705_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='VestAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('account', models.CharField(max_length=32, unique=True, verbose_name='账号')),
                ('gender', models.CharField(max_length=32, verbose_name='账号性别', choices=[('1', '男'), ('0', '女')])),
                ('name', models.CharField(max_length=128, verbose_name='账号昵称', null=True, blank=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('alter_time', models.DateTimeField(auto_now=True, verbose_name='最近修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='VestInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('owner', models.CharField(max_length=128, verbose_name='姓名')),
                ('position', models.CharField(max_length=128, verbose_name='职位', null=True, blank=True)),
                ('order', models.IntegerField(verbose_name='序号', default=0, help_text='值越小，同分类中越靠前显示')),
                ('show_status', models.BooleanField(max_length=32, verbose_name='显示状态', default=True, help_text='是否显示到网站')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('alter_time', models.DateTimeField(auto_now=True, verbose_name='最近修改时间')),
                ('id_info', models.ManyToManyField(verbose_name='账号信息', to='xuegod.VestAccount', related_name='id_set')),
            ],
        ),
        migrations.AlterModelOptions(
            name='indexnav',
            options={'verbose_name': '导航网址', 'verbose_name_plural': '导航网址列表'},
        ),
        migrations.AlterModelOptions(
            name='indextype',
            options={'verbose_name': '导航类型', 'verbose_name_plural': '导航类型列表'},
        ),
    ]
