# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order_lifecycle_management', '0008_auto_20170818_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 13, 11, 39, 926491, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
