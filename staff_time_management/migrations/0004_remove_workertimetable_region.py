# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff_time_management', '0003_workertimetable_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workertimetable',
            name='region',
        ),
    ]
