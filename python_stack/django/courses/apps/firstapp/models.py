# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):     #Class tends to be singular
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)    #will add time at creation once
    updated_at = models.DateTimeField(auto_now=True)        #will add time everytime it updates
