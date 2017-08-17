# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0015_remove_addontype_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='addontype',
            name='title',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
