# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Nutrients(models.Model):
    user = models.ForeignKey('auth.User')
    date = models.DateField(null=False, default=timezone.now)
    name = models.CharField(max_length=300, null=False)
    amount = models.FloatField(max_length=10, default=0, null=False)
    meal = models.CharField(max_length=9, null=False, default='snack')
    energy_kJ = models.FloatField(max_length=10, default=0)
    energy_kcal = models.FloatField(max_length=10, default=0)
    protein = models.FloatField(max_length=10, default=0)
    carbs = models.FloatField(max_length=10, default=0)
    fat = models.FloatField(max_length=10, default=0)
    sugar = models.FloatField(max_length=10, default=0)
    fiber = models.FloatField(max_length=10, default=0)

    def __unicode__(self):
        return self.name


