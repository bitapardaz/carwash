# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0007_auto_20170805_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicetype',
            name='movie_link',
        ),
        migrations.AddField(
            model_name='addon',
            name='movie_link',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='addon',
            name='read_more',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='addontype',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addontype',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='movie_link',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
    ]
