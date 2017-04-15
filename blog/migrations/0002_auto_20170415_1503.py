# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
