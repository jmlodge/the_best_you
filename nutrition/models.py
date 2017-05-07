# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Nutrients(models.Model):
    name = models.CharField(max_length=200, null=False)
    energy_kJ = models.FloatField
    energy_kcal = models.FloatField
    protein = models.FloatField
    carbs = models.FloatField
    fat = models.FloatField
    sugar = models.FloatField
    fiber = models.FloatField
