# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_task',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_time',
            new_name='time',
        ),
    ]