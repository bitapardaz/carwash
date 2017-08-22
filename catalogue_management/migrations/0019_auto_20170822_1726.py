# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0018_service_display_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addontypeservicetypedependency',
            name='addon',
            field=models.ForeignKey(to='catalogue_management.AddOnType'),
        ),
    ]
