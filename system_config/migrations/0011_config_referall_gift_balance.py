# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0010_config_carwash_add_on_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='referall_gift_balance',
            field=models.IntegerField(default=10000),
        ),
    ]
