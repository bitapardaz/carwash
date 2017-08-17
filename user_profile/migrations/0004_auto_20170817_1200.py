# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0003_auto_20170817_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=100, null=True, blank=True)),
                ('token_expiry', models.DateTimeField(null=True, blank=True)),
                ('rate', models.IntegerField(default=10)),
                ('mobile_number', models.CharField(max_length=15)),
                ('otp_code', models.CharField(max_length=100, null=True, blank=True)),
                ('otp_expiration', models.DateTimeField(null=True, blank=True)),
                ('age', models.IntegerField(default=0)),
                ('number_of_cancellation', models.IntegerField(default=0)),
                ('is_into_cars', models.BooleanField(default=0)),
                ('likes_offroad', models.BooleanField(default=0)),
                ('gender', models.ForeignKey(to='user_profile.Gender')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user_type', models.ForeignKey(blank=True, to='user_profile.UserType', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='user_type',
        ),
        migrations.DeleteModel(
            name='CustomerProfile',
        ),
    ]
