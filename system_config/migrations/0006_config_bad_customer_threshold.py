# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0005_config_inventory_item_processing_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='bad_customer_threshold',
            field=models.IntegerField(default=4),
        ),
    ]
