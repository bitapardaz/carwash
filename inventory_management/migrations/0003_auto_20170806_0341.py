# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0002_inventoryrequest_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_type', models.CharField(max_length=10)),
                ('unit', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='item_type',
            field=models.ForeignKey(blank=True, to='inventory_management.InventoryItemType', null=True),
        ),
    ]
