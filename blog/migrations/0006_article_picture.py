# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-31 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180531_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.TextField(default=0, verbose_name='\u56fe\u7247\u5730\u5740'),
            preserve_default=False,
        ),
    ]
