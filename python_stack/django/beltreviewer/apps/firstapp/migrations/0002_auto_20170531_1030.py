# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=b'First', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=b'Last', max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='user',
            name='alias',
            field=models.CharField(max_length=55),
        ),
    ]
