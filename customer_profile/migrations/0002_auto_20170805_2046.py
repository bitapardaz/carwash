# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarWasherProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images')),
                ('description', models.CharField(max_length=100)),
                ('balance', models.IntegerField(default=0)),
                ('national_number', models.CharField(max_length=12)),
                ('id_scan_1', models.ImageField(upload_to=b'images')),
                ('id_scan_2', models.ImageField(upload_to=b'images')),
                ('id_scan_3', models.ImageField(upload_to=b'images')),
                ('total_time_available', models.IntegerField(default=0)),
                ('total_orders_per_last_day', models.IntegerField(default=0)),
                ('total_orders_current_week', models.IntegerField(default=0)),
                ('total_orders_current_month', models.IntegerField(default=0)),
                ('rate_of_cancellation', models.IntegerField(default=0)),
                ('load', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupervisorProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='user_type',
            field=models.ForeignKey(to='customer_profile.UserType'),
        ),
    ]
