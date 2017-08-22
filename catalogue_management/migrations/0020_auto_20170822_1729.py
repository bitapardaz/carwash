# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue_management', '0019_auto_20170822_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addon',
            old_name='movie_link',
            new_name='short_description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='movie_link',
        ),
        migrations.AddField(
            model_name='addontype',
            name='movie_link',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='addontype',
            name='read_more',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='addontype',
            name='short_description',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='servicetype',
            name='movie_link',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
