# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_lifecycle_management', '0002_order_ram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ram',
        ),
    ]
