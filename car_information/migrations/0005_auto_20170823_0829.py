# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_information', '0004_auto_20170817_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartype',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartype',
            name='icon',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
    ]
