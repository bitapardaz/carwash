# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_promotioncode_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotioncode',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 9, 22, 54, 851785, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
