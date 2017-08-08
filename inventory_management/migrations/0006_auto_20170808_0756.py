# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0005_auto_20170806_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryrequest',
            name='delivery_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='inventoryrequest',
            name='request_time',
            field=models.DateTimeField(),
        ),
    ]
