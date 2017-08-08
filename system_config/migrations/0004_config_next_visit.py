# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0003_auto_20170806_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='next_visit',
            field=models.IntegerField(default=10),
        ),
    ]
