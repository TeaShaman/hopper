# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-21 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopper', '0022_auto_20171021_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventcompleted',
            name='date_modified',
        ),
        migrations.AddField(
            model_name='event',
            name='date_completed',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]