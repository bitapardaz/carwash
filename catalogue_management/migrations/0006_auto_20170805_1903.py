# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0005_auto_20170805_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='movie_link',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='servicetype',
            name='read_more',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
