# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20170602_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.User'),
        ),
    ]
