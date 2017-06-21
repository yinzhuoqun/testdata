# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0004_auto_20170510_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestDevice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('device_order', models.IntegerField(verbose_name='序号', help_text='值越小，同分类中越靠前显示', default=0)),
                ('device_name', models.CharField(max_length=128, help_text='设备的中文名称', verbose_name='设备名称')),
                ('device_screen_size', models.CharField(null=True, help_text='单位：英寸，如：5.5', max_length=48, blank=True, verbose_name='屏幕尺寸')),
                ('device_screen_resolution', models.CharField(null=True, help_text='单位：像素，如：1920*1080', max_length=48, blank=True, verbose_name='分辨率')),
                ('device_platfrom', models.CharField(choices=[('1', 'Android'), ('2', 'iOS'), ('0', 'other')], max_length=48, verbose_name='系统平台')),
                ('device_platfrom_version', models.CharField(null=True, help_text='如：4.3', max_length=48, blank=True, verbose_name='系统版本')),
                ('use_name', models.CharField(null=True, help_text='如：张三', max_length=128, blank=True, verbose_name='领用人员')),
                ('use_time', models.DateTimeField(verbose_name='领用日期', auto_now_add=True)),
                ('return_time', models.DateTimeField(null=True, verbose_name='归还日期', blank=True)),
                ('alter_time', models.DateTimeField(auto_now=True, verbose_name='最近修改时间')),
                ('device_show_status', models.CharField(choices=[('1', '显示'), ('0', '隐藏')], max_length=48, verbose_name='是否显示到网页', default='显示')),
                ('note', models.TextField(null=True, max_length=256, blank=True, verbose_name='备注')),
            ],
        ),
    ]
