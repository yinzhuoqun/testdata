# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xuegod', '0020_auto_20170710_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('position_type', models.CharField(blank=True, verbose_name='职位名称', null=True, max_length=128)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('alter_time', models.DateTimeField(verbose_name='最近修改时间', auto_now=True)),
            ],
            options={
                'verbose_name_plural': '职位名称列表',
                'verbose_name': '职位名称',
            },
        ),
        migrations.AlterField(
            model_name='vestinfo',
            name='id_info',
            field=models.ManyToManyField(to='xuegod.VestAccount', help_text='1 是男性，0 是女性', verbose_name='账号信息', related_name='id_set'),
        ),
        migrations.AlterField(
            model_name='vestinfo',
            name='position',
            field=models.ForeignKey(to='xuegod.PositionType', verbose_name='职位昵称', related_name='position_set'),
        ),
    ]
