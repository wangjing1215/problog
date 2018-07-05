# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BlogMoudel(models.Model):
    contact_name = models.CharField(
        u'文章标题',
        max_length=50,
        default='',
        blank=True,
        help_text=u'文章标题',
    )
    contact_phone = models.CharField(
        u'概括',
        max_length=200,
        default='',
        blank=True,
        help_text=u'概括',
    )
    loan_amount = models.DecimalField(
        u'标签',
        max_length=10,
        default='',
        blank=True,
        help_text=u'标签',
    )
    loan_number = models.CharField(
        u'贷款编号',
        max_length=50,
        help_text=u'贷款编号',
    )
    start_date = models.DateField(
        u'开始日期',
        null=True,
        help_text=u'开始日期',
    )