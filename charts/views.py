# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from nutrition.models import Nutrients
from django.utils import timezone
from datetime import timedelta
from services import chart_service, energy_service


def get_chart_data(request):
    # if request.method == 'POST':
    #    date = request.POST['date']

    user = request.user.id
    today = timezone.now()
    yesterday = today - timedelta(days=1)

    labels = ["Protein", "Carbohydrates", "Fat", "Sugar", "Fiber"]
    todays_items = chart_service(today, user)
    yesterdays_items = chart_service(yesterday, user)
    # previous_items = chart_service(date, user)
    data = {
        "labels": labels,
        "today_d": todays_items,
        "yesterday_d": yesterdays_items,
        # "previous_d": previous_items
    }
    return JsonResponse(data)


def get_energy_data(request):

    user = request.user.id

    past_week_energy = energy_service(user)
    labels = ["today - 6", "today - 5", "today - 4", "today - 3", "today - 2", "today - 1", "today"]

    energy_data = {
        "labels": labels,
        "past_week_energy": past_week_energy
    }

    return JsonResponse(energy_data)


def get_previous_data(request):
    if request.method == 'POST':
        date = request.POST['date']
        user = request.user.id
        labels = ["Protein", "Carbohydrates", "Fat", "Sugar", "Fiber"]
        items = chart_service(date, user)
        previous_data = {
            "labels": labels,
            "previous_d": items,
        }
        return JsonResponse(previous_data)

