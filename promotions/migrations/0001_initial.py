# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000)),
                ('code', models.CharField(max_length=100)),
                ('valid_from', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to=b'images')),
            ],
        ),
    ]
