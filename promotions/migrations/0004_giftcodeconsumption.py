# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promotions', '0003_promotioncode_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCodeConsumption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_consumed', models.DateTimeField(auto_now=True)),
                ('promotion_code', models.ForeignKey(to='promotions.PromotionCode')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
