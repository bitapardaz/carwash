# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0010_servicetype_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='icon',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
    ]
