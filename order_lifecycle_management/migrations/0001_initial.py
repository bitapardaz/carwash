# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('car_information', '0004_auto_20170817_1116'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0006_auto_20170818_0933'),
        ('catalogue_management', '0016_addontype_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=1000)),
                ('original_price', models.IntegerField(default=0)),
                ('was_elibible_for_discount', models.BooleanField(default=False)),
                ('discount', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('payment_rrn', models.CharField(max_length=20)),
                ('alert', models.BooleanField(default=False)),
                ('worker_heads_off_at', models.DateTimeField(null=True, blank=True)),
                ('worker_arrived_at', models.DateTimeField(null=True, blank=True)),
                ('worker_finished_at', models.DateTimeField(null=True, blank=True)),
                ('service_duration', models.IntegerField(default=0)),
                ('cancelled', models.BooleanField(default=False)),
                ('changed', models.BooleanField(default=False)),
                ('address', models.ForeignKey(to='user_profile.KnownAdresses')),
                ('car_type', models.ForeignKey(to='car_information.CarType')),
                ('customer_id', models.ForeignKey(related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('display_order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentChannel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('display_order', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment_channel',
            field=models.ForeignKey(to='order_lifecycle_management.PaymentChannel'),
        ),
        migrations.AddField(
            model_name='order',
            name='service_type',
            field=models.ForeignKey(to='catalogue_management.Service'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(to='order_lifecycle_management.OrderStatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='worker',
            field=models.ForeignKey(related_name='worker', to=settings.AUTH_USER_MODEL),
        ),
    ]
