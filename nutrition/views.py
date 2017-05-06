# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from the_best_you.settings import USDA_API_KEY
from django.shortcuts import render, HttpResponse
import requests
import json


def search_name(request):
    parsed_data = []
    if request.method == 'POST':
        food = request.POST.get('food')
        parameters = {"api_key": USDA_API_KEY, "q": food, "ds": "Standard Reference"}
        json_list = []
        req = requests.get('https://api.nal.usda.gov/ndb/search/?format=json&sort=r&max=10&offset=0', params=parameters)
        json_list.append(json.loads(req.content))

        # check to see how many foods are returned
        for i in json_list:
            end = i['list']['end']

            p = 0
            while p < end:
                for data in json_list:
                    food_data = {'name': data['list']['item'][p]['name'], 'ndbno': data['list']['item'][p]['ndbno']}
                    parsed_data.append(food_data)
                    p += 1

    return render(request, 'nutrition/foodsearch.html', {'data': parsed_data})


def get_nutrients(request):
    parsed_data = []
    nutrients = ["204", "203", "205", "208", "268", "269", "291"]
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        parameters = {"api_key": USDA_API_KEY, "nutrients": nutrients, "ndbno": food_id}
        json_list = []
        req = requests.get(' https://api.nal.usda.gov/ndb/nutrients/?format=json', params=parameters)
        json_list.append(json.loads(req.content))

        for data in json_list:
            nutrient_data = {'name': data['report']['foods'][0]['name'],
                             'Energy_kJ': data['report']['foods'][0]['nutrients'][0]['gm'],
                             'Protein': data['report']['foods'][0]['nutrients'][1]['gm'],
                             'Sugar': data['report']['foods'][0]['nutrients'][2]['gm'],
                             'Fat': data['report']['foods'][0]['nutrients'][3]['gm'],
                             'Carbohydrates': data['report']['foods'][0]['nutrients'][4]['gm'],
                             'Energy_kcal': data['report']['foods'][0]['nutrients'][5]['gm'],
                             'Fiber': data['report']['foods'][0]['nutrients'][6]['gm']}
            parsed_data.append(nutrient_data)

    # return HttpResponse(req.content)
    return render(request, 'nutrition/foodsearch.html', {'nutrient_data': parsed_data})
    # return HttpResponse(parsed_data)

