# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region_management', '0002_auto_20170822_1751'),
        ('order_lifecycle_management', '0009_order_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='region',
            field=models.ForeignKey(blank=True, to='region_management.Region', null=True),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
    ]
