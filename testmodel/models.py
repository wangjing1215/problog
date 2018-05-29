from __future__ import unicode_literals

from django.db import models

class Citys(models.Model):
    addoid=models.CharField(max_length=8)
    oid = models.CharField(max_length=8)
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=24)
    province_code = models.CharField(max_length=8)

    def __unicode__(self):
        return self.name

class Districts(models.Model):
    addoid = models.CharField(max_length=8)
    oid = models.CharField(max_length=8)
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=24)
    city_code = models.CharField(max_length=8)

class Provinces(models.Model):
    addoid = models.CharField(max_length=8)
    oid = models.CharField(max_length=8)
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=24)