# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_lifecycle_management', '0006_auto_20170818_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
    ]
