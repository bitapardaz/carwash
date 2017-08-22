# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0016_addontype_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddonTypeServiceTypeDependency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('addon', models.ForeignKey(to='catalogue_management.AddOn')),
            ],
        ),
        migrations.AddField(
            model_name='servicetype',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addontypeservicetypedependency',
            name='base',
            field=models.ForeignKey(to='catalogue_management.ServiceType'),
        ),
    ]
