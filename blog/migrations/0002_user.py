# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-29 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('password', models.TextField(verbose_name='password')),
            ],
        ),
    ]
