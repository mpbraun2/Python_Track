# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20170602_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default='2000-10-10', max_length=8),
        ),
    ]
