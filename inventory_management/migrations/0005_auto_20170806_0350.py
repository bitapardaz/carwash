# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0004_inventoryrequest_alarm_raised'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryrequest',
            old_name='delivery_tiem',
            new_name='delivery_time',
        ),
        migrations.AddField(
            model_name='inventoryrequest',
            name='delivery_location',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
