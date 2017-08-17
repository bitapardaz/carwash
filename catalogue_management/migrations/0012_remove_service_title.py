# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0011_servicetype_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='title',
        ),
    ]
