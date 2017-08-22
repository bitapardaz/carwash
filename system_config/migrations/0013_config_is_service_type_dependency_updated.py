# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0012_remove_config_referall_gift_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='is_service_type_dependency_updated',
            field=models.BooleanField(default=False),
        ),
    ]
