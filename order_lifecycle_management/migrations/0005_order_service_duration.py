# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_lifecycle_management', '0004_remove_order_service_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='service_duration',
            field=models.IntegerField(default=0),
        ),
    ]
