from django.shortcuts import render, HttpResponse
from api_config.open_weather_map import WeatherApi
import requests
import json
# Create your views here.


def index(request, filters=None):
    return HttpResponse('HelloWorld')


def profile(request, city='london', period='current'):
    jsonList = []
    s = WeatherApi(city=city)
    json_data = s.get_json_feed(period=period)
    if period == 'five_day':
        json_data = s.forecast_calculations(json_data=json_data)

    return HttpResponse(json.dumps(json_data), content_type="application/json")
