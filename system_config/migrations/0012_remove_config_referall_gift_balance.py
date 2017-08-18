# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0011_config_referall_gift_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='referall_gift_balance',
        ),
    ]
