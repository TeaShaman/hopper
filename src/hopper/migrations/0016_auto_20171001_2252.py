# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-01 22:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hopper', '0015_auto_20170208_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='guidebook_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='online_desc',
            new_name='internal',
        ),
        migrations.RemoveField(
            model_name='event',
            name='complete',
        ),
        migrations.AddField(
            model_name='event',
            name='event_organiser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='last_confirmed',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
