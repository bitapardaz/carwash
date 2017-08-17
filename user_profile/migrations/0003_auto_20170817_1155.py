# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20170817_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='token',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='token_expiry',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
