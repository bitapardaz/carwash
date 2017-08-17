# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0014_addontype_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addontype',
            name='title',
        ),
    ]
