# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0004_auto_20170817_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_into_cars', models.BooleanField(default=0)),
                ('likes_offroad', models.BooleanField(default=0)),
                ('last_carwash_request', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_into_cars',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='likes_offroad',
        ),
        migrations.AddField(
            model_name='carwasherprofile',
            name='last_carwash_service',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
