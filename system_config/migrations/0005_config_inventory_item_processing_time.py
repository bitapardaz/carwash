# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0004_config_next_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='inventory_item_processing_time',
            field=models.IntegerField(default=10),
        ),
    ]
