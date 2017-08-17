# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_information', '0003_car_car_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='subtitle',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
