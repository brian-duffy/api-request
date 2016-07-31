import unittest
from open_weather_map import WeatherApi

class TestOpenWeatherMap(unittest.TestCase):
    pass_city = 'dubai'
    edgecase_city = 'San Francisco'
    fail_city = 'ndnuqwnd'

    def test_get_lat_lon_simple(self):
        s = WeatherApi(city=self.pass_city)
        self.assertIsNotNone(s.lat, s.lon)

    def test_get_lat_lon_edgecase(self):
        s = WeatherApi(city=self.edgecase_city)
        self.assertIsNotNone(s.lat, s.lon)

    def test_no_result(self):
        s = WeatherApi(self.fail_city)
        self.assertEqual([s.lat, s.lon], [999999, 999999])

    def test_get_json_feed_current(self):
        json = WeatherApi(city=self.pass_city).get_json_feed(period='current')
        self.assertIn('weather', json)

    def test_get_json_feed_current_no_result(self):
        json = WeatherApi(city=self.fail_city).get_json_feed(period='current')
        self.assertNotIn('weather', json)

    def test_get_json_feed_forecast(self):
        json = WeatherApi(city=self.pass_city).get_json_feed(period='forecast')
        self.assertIn('city', json)

    def test_get_json_forecast_calculations(self):
        s = WeatherApi(city=self.pass_city)
        json = s.get_json_feed(period='forecast')
        self.assertIn('humidity_calcs', s.forecast_calculations(json_data=json))

    def test_get_json_forecast_calculations_no_result(self):
        s = WeatherApi(city=self.fail_city)
        json = s.get_json_feed(period='forecast')
        self.assertNotIn('humidity_calcs', s.forecast_calculations(json_data=json))

if __name__ == '__main__':
    unittest.main()