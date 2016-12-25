# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import hopper.models


class Migration(migrations.Migration):

    dependencies = [
        ('hopper', '0003_auto_20161225_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='resourceId',
            field=models.ForeignKey(default=1, on_delete=models.SET(hopper.models.get_default_room), to='hopper.Room'),
            preserve_default=False,
        ),
    ]
