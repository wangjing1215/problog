# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-31 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_jianshu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='jianshu',
            field=models.TextField(verbose_name='\u6982\u8981'),
        ),
    ]
