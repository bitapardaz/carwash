# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryDeliveryStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'images')),
                ('tracking_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_time', models.DateTimeField(auto_now=True)),
                ('delivery_tiem', models.DateTimeField(auto_now=True)),
                ('comments', models.CharField(max_length=1000)),
                ('item', models.ForeignKey(to='inventory_management.InventoryItem')),
                ('status', models.ForeignKey(to='inventory_management.InventoryDeliveryStatus')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
