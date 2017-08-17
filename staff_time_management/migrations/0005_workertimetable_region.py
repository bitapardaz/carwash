# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region_management', '0001_initial'),
        ('staff_time_management', '0004_remove_workertimetable_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='workertimetable',
            name='region',
            field=models.ForeignKey(blank=True, to='region_management.Region', null=True),
        ),
    ]
