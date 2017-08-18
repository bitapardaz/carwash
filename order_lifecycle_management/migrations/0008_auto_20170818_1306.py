# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_lifecycle_management', '0007_auto_20170818_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='service_type',
            new_name='service',
        ),
    ]
