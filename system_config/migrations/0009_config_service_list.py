# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0008_auto_20170817_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='service_list',
            field=models.BooleanField(default=False),
        ),
    ]
