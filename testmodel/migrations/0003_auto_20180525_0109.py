# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-25 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0002_auto_20180523_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='citys',
            name='addoid',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='districts',
            name='addoid',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provinces',
            name='addoid',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
    ]
