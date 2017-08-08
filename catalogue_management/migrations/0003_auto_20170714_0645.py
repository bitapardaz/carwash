# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='car_type',
            field=models.ForeignKey(blank=True, to='catalogue_management.CarType', null=True),
        ),
    ]
