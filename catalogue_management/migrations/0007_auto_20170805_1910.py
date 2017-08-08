# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0006_auto_20170805_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addon',
            name='car_type',
            field=models.ForeignKey(to='car_information.CarType'),
        ),
        migrations.AlterField(
            model_name='service',
            name='car_type',
            field=models.ForeignKey(blank=True, to='car_information.CarType', null=True),
        ),
        migrations.DeleteModel(
            name='CarType',
        ),
    ]
