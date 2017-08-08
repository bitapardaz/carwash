# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0002_alerttext'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='interconnection_time',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='config',
            name='slack_time',
            field=models.IntegerField(default=10),
        ),
    ]
