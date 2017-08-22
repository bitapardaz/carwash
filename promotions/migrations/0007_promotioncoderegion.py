# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region_management', '0001_initial'),
        ('promotions', '0006_auto_20170818_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionCodeRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promotion_code', models.ForeignKey(to='promotions.PromotionCode')),
                ('region', models.ForeignKey(to='region_management.Region')),
            ],
        ),
    ]
