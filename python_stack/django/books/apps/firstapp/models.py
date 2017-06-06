# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):     #Class tends to be singular
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    published_date = models.CharField(max_length=6)
    category = models.CharField(max_length=15)
    in_print = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)    #will add time at creation once
    updated_at = models.DateTimeField(auto_now=True)
