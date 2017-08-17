# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('region_management', '0001_initial'),
        ('car_information', '0002_cartype'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('user', models.ForeignKey(related_name='main_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField(default=10)),
                ('mobile_number', models.CharField(max_length=15)),
                ('otp_code', models.CharField(max_length=100, null=True, blank=True)),
                ('otp_expiration', models.DateTimeField(null=True, blank=True)),
                ('age', models.IntegerField(default=0)),
                ('number_of_cancellation', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='KnownAdresses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('date_verified', models.DateField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KnownCar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateField()),
                ('last_visit', models.DateField()),
                ('next_visit_reminder', models.DateField()),
                ('car', models.ForeignKey(to='car_information.Car')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MobileDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_title', models.CharField(max_length=200)),
                ('device_token', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupervisorProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('regions', models.ManyToManyField(to='region_management.Region')),
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
            model_name='customerprofile',
            name='gender',
            field=models.ForeignKey(to='user_profile.Gender'),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='user_type',
            field=models.ForeignKey(blank=True, to='user_profile.UserType', null=True),
        ),
    ]
