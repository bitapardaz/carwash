# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0017_auto_20170822_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
    ]
