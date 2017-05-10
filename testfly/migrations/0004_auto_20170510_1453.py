# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfly', '0003_testreport_test_regression'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buginfo',
            options={'verbose_name_plural': '提交 Bug 统计列表', 'verbose_name': '提交 Bug 统计'},
        ),
        migrations.AlterModelOptions(
            name='bugsurplusinfo',
            options={'verbose_name_plural': '遗留 Bug 统计列表', 'verbose_name': '遗留 Bug 统计'},
        ),
        migrations.AlterModelOptions(
            name='testparticipants',
            options={'verbose_name_plural': '测试参与人员列表', 'verbose_name': '测试参与人员'},
        ),
    ]
