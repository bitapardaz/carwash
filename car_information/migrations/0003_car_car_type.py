# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_information', '0002_cartype'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(blank=True, to='car_information.CarType', null=True),
        ),
    ]
