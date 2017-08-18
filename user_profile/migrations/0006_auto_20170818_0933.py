# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20170817_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumerprofile',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='consumerprofile',
            name='gift_balance',
            field=models.IntegerField(default=0),
        ),
    ]
