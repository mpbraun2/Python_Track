# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20170531_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='alias',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]