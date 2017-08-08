# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0003_auto_20170714_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.CharField(default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AddOnType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='addon',
            name='addon_type',
            field=models.ForeignKey(to='catalogue_management.AddOnType'),
        ),
        migrations.AddField(
            model_name='addon',
            name='car_type',
            field=models.ForeignKey(to='catalogue_management.CarType'),
        ),
    ]
