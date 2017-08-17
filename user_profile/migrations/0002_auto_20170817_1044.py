# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='is_into_cars',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='likes_offroad',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='knowncar',
            name='plate_number',
            field=models.CharField(default='111', max_length=100),
            preserve_default=False,
        ),
    ]
