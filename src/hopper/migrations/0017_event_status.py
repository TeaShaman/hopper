# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-08 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopper', '0016_auto_20171001_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[(b'D', b'DRAFT'), (b'R', b'REVIEW'), (b'C', b'COMPLETED'), (b'A', b'AMENDED')], default=b'D', max_length=1),
        ),
    ]
