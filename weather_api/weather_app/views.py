from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from api_config.open_weather_map import WeatherApi
from api_config.bar_chart import get_bar_chart
import urllib2
import json
# Create your views here.


def index(request, filters=None):
    return HttpResponse('HelloWorld')


def web_api(request, city='london', period='current', bar_chart=None):
    s = WeatherApi(city=city)
    try:
        json_data = s.get_json_feed(period=period)
        if period == 'forecast':
            json_data = s.forecast_calculations(json_data=json_data)
    except (urllib2.HTTPError, urllib2.URLError):
            return HttpResponseNotFound('<h1>Page not found</h1>')
    except KeyError:
        return HttpResponseNotFound("<h1>Page not found. Selection must be 'current' or 'forecast'</h1>")
    else:
        chart = get_bar_chart(data=json_data)
        context = {'chart': chart}
        if bar_chart:
            template = loader.get_template('weather_app/profile.html')
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse(json.dumps(json_data), content_type="application/json")
