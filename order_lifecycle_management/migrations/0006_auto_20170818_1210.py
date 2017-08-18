# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_lifecycle_management', '0005_order_service_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='total_price',
        ),
    ]
