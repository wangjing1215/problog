# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-23 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citys',
            name='oid',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='districts',
            name='oid',
            field=models.CharField(default='1', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provinces',
            name='oid',
            field=models.CharField(default='111', max_length=8),
            preserve_default=False,
        ),
    ]
