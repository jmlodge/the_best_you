# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170424_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='stripe_id',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subscription_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
