# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0003_auto_20170806_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryrequest',
            name='alarm_raised',
            field=models.BooleanField(default=False),
        ),
    ]
