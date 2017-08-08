# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0008_auto_20170805_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='addon',
            name='duration',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='service',
            name='duration',
            field=models.IntegerField(default=10),
        ),
    ]
