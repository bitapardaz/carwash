# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0009_auto_20170806_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='short_description',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
