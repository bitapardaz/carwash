# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0005_auto_20170818_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralGift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('valid_from', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
                ('text_shown_to_customer_first_line', models.CharField(max_length=1000)),
                ('text_shown_to_customer_second_line', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ReferralGiftType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='referralhistory',
            name='was_rewarded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='referralgift',
            name='gift_type',
            field=models.ForeignKey(to='promotions.ReferralGiftType'),
        ),
        migrations.AddField(
            model_name='referralhistory',
            name='reward',
            field=models.ForeignKey(blank=True, to='promotions.ReferralGift', null=True),
        ),
    ]
