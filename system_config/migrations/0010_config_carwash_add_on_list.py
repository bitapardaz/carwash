# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0009_config_service_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='carwash_add_on_list',
            field=models.BooleanField(default=False),
        ),
    ]
