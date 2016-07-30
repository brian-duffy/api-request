import urllib
import urllib2
import numpy
import json
from geopy.geocoders import Nominatim
from open_weather_map_config import *


class WeatherApi(object):
    """
    Class to use a city and period and return a json string.
    """
    def __init__(self, city=None, period=None):
        """
        :param city: City used to get the weather for. A best guess will be used if there are multiple results.
        :param period: Period used to get the weather for. Can be either 'current' or 'five_day' (limited by api).
        """
        self.city = city
        self.period = period
        self.lat, self.lon = self.get_lat_lon(city=city)

    @staticmethod
    def get_lat_lon(city=None):
        """
        Function to return a latitude and longitude coordinates of a given city.
        :param city: City to search for.
        :return: Returns lat/lon values. Returns 999999 if no locations found.
        """
        geolocator = Nominatim()
        try:
            loc = geolocator.geocode(city)
            return loc.latitude, loc.longitude
        except (TypeError, AttributeError):
            return 999999, 999999

    def get_json_feed(self, period='current'):
        """
        Using the latitude and longitude of a city, this function gets the required period
        :param period: Period to search for, either current or five_day
        :return: JSON feed with raw data
        """
        if period == 'five_day':
            base_url = forecast_base_url
        else:
            base_url = current_weather_base_url
        json_url = base_url + end_url.format(self.lat, self.lon, api_key)
        result = urllib2.urlopen(json_url).read()
        return json.loads(result)

    @staticmethod
    def forecast_calculations(json_data=None):
        """
        Function used to calculate min, max, average and median temperature and humidity for supplied location.
        :param json_data:
        :return: returns json_data appended with new calculated values
        """
        all_temps = [x['main']['temp'] for i, x in(enumerate(json_data['list']))]
        all_humidities = [x['main']['humidity'] for i, x in(enumerate(json_data['list']))]

        def get_all(list_of_calculations=None):
            calcs = {}
            min_temp = min(list_of_calculations)
            max_temp = max(list_of_calculations)
            average = reduce(lambda x, y: x + y, list_of_calculations) / len(list_of_calculations)
            median = numpy.median(numpy.array(list_of_calculations))
            for y in ('min_temp', 'max_temp', 'average', 'median'):
                calcs[y] = locals()[y]
            return calcs
        json_data['temperature_calcs'] = get_all(list_of_calculations=all_temps)
        json_data['humidity_calcs'] = get_all(list_of_calculations=all_humidities)
        return json_data


