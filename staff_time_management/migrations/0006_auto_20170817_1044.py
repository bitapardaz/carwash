# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff_time_management', '0005_workertimetable_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='title',
        ),
        migrations.AddField(
            model_name='timeslot',
            name='day',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
