# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-30 07:30
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u535a\u5ba2\u6807\u7b7e'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='\u6587\u7ae0\u6b63\u6587'),
        ),
    ]
