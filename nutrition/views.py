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

        print(req.content)

        for i in json_list:
            end = i['list']['end']

            p = 0
            while p < end:
                for data in json_list:
                    food_data = {'name': data['list']['item'][p]['name'], 'ndbno': data['list']['item'][p]['ndbno']}
                    parsed_data.append(food_data)
                    p += 1

        # return HttpResponse(parsed_data)
    return render(request, 'nutrition/foodsearch.html', {'data': parsed_data})


def get_nutrients(request):
    nutrients = ["204", "203", "205", "208", "268", "269", "291"]
    parameters = {"api_key": USDA_API_KEY, "nutrients": nutrients, "ndbno": "01005"}
    req = requests.get(' https://api.nal.usda.gov/ndb/nutrients/?format=json', params=parameters)
    content = req.text
    return HttpResponse(content)

