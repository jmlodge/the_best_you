# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170424_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Training', 'Training'), ('Mindset', 'Mindset'), ('Nutrition', 'Nutrition'), ('General', 'General')], default='General', max_length=9),
        ),
    ]