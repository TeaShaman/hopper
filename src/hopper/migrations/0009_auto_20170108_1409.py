# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hopper', '0008_auto_20161226_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='resourceId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hopper.Room'),
        ),
    ]