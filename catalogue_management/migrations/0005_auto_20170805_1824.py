# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0004_auto_20170727_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
