# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from nutrition.models import Nutrients
from django.utils import timezone
from datetime import timedelta
from accounts.models import User


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        user = request.user.id
        today = timezone.now()
        yesterday = today - timedelta(days=1)
        today_nutrients = Nutrients.objects.filter(date=today).values(
            'protein', 'carbs', 'fat', 'sugar', 'fiber', 'amount'
        )
        yesterdays_nutrients = Nutrients.objects.filter(date=yesterday).values(
            'protein', 'carbs', 'fat', 'sugar', 'fiber', 'amount'
        )
        protein_list = []
        carbs_list = []
        fat_list = []
        sugar_list = []
        fiber_list = []

        protein_list_y = []
        carbs_list_y = []
        fat_list_y = []
        sugar_list_y = []
        fiber_list_y = []

        for item in today_nutrients:
            p = item['protein']
            c = item['carbs']
            f = item['fat']
            s = item['sugar']
            fi = item['fiber']
            a = item['amount']

            p_amount = (p / 100) * a
            protein_list.append(p_amount)
            c_amount = (c / 100) * a
            carbs_list.append(c_amount)
            f_amount = (f / 100) * a
            fat_list.append(f_amount)
            s_amount = (s / 100) * a
            sugar_list.append(s_amount)
            fi_amount = (fi / 100) * a
            fiber_list.append(fi_amount)

        protein = float("%.2f" % sum(protein_list))
        carbs = float("%.2f" % sum(carbs_list))
        fat = float("%.2f" % sum(fat_list))
        sugar = float("%.2f" % sum(sugar_list))
        fiber = float("%.2f" % sum(fiber_list))

        for item in yesterdays_nutrients:
            p = item['protein']
            c = item['carbs']
            f = item['fat']
            s = item['sugar']
            fi = item['fiber']
            a = item['amount']

            p_amount = (p / 100) * a
            protein_list_y.append(p_amount)
            c_amount = (c / 100) * a
            carbs_list_y.append(c_amount)
            f_amount = (f / 100) * a
            fat_list_y.append(f_amount)
            s_amount = (s / 100) * a
            sugar_list_y.append(s_amount)
            fi_amount = (fi / 100) * a
            fiber_list_y.append(fi_amount)

        protein_y = float("%.2f" % sum(protein_list_y))
        carbs_y = float("%.2f" % sum(carbs_list_y))
        fat_y = float("%.2f" % sum(fat_list_y))
        sugar_y = float("%.2f" % sum(sugar_list_y))
        fiber_y = float("%.2f" % sum(fiber_list_y))

        labels = ["Protein", "Carbohydrates", "Fat", "Sugar", "Fiber"]
        todays_items = [protein, carbs, fat, sugar, fiber]
        yesterdays_items = [protein_y, carbs_y, fat_y, sugar_y, fiber_y]
        data = {
            "labels": labels,
            "today_d": todays_items,
            "yesterday_d": yesterdays_items,
        }
        return Response(data)

