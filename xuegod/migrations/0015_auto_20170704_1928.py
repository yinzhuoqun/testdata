# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0014_homepage_url_status_use'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexNav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('url', models.CharField(verbose_name='网址', max_length=256)),
                ('fullname', models.CharField(verbose_name='显示名称', max_length=256)),
                ('nickname', models.CharField(verbose_name='简短名称', null=True, max_length=256, blank=True)),
                ('order', models.IntegerField(verbose_name='序号', default=0, help_text='值越小，同分类中越靠前显示')),
                ('show_status', models.BooleanField(verbose_name='显示状态', help_text='是否显示到网站', default=True, max_length=32)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('alter_time', models.DateTimeField(verbose_name='最近修改时间', auto_now=True)),
            ],
            options={
                'verbose_name': '首页导航',
                'verbose_name_plural': '首页导航列表',
            },
        ),
        migrations.CreateModel(
            name='IndexType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('url_type', models.CharField(verbose_name='类型', help_text='自定义类型，方便区分', default='other', max_length=32)),
            ],
            options={
                'verbose_name': '网址类型',
                'verbose_name_plural': '网址类型列表',
            },
        ),
        migrations.AlterField(
            model_name='testid',
            name='user_id',
            field=models.IntegerField(verbose_name='账号', unique=True),
        ),
        migrations.AddField(
            model_name='indexnav',
            name='url_type',
            field=models.ForeignKey(verbose_name='分类', to='xuegod.IndexType'),
        ),
    ]
