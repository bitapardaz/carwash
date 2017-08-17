# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0006_config_bad_customer_threshold'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='absence_threshold_days',
            field=models.IntegerField(default=10),
        ),
    ]
