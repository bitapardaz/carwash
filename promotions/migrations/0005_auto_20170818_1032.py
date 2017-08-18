# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promotions', '0004_giftcodeconsumption'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_date', models.DateTimeField(auto_now=True)),
                ('new_commer', models.ForeignKey(related_name='destination', to=settings.AUTH_USER_MODEL)),
                ('referred', models.ForeignKey(related_name='source', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='promotioncode',
            name='QR_code',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
    ]
