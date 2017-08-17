# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0007_config_absence_threshold_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='carwash_add_on_list',
        ),
        migrations.RemoveField(
            model_name='config',
            name='service_list',
        ),
    ]
