# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from the_best_you.settings import USDA_API_KEY
from django.shortcuts import render, HttpResponse
import requests
import json


def search_name(request):
    parameters = {"api_key": USDA_API_KEY, "q": "baked beans"}
    json_list = []
    req = requests.get('https://api.nal.usda.gov/ndb/search/?format=json&sort=n&max=10&offset=0', params=parameters)
    json_list.append(json.loads(req.content))
    parsed_data = []
    i = 0
    while i < 5:
        for data in json_list:
            food_data = {}
            food_data['name'] = data['list']['item'][i]['name']
            food_data['ndbno'] = data['list']['item'][i]['ndbno']
            parsed_data.append(food_data)
            i += 1
    return HttpResponse(parsed_data)
