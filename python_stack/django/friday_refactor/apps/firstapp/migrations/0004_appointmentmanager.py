# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20170602_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
