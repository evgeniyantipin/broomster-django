# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160302_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='apt',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='quote',
            name='city',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='extras',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='first_name',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='last_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='state',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='street_address',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
