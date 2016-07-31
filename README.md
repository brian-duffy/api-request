# Weather API

JSON API to output weather statistics and bar charts.

## Usage

##### API is accessible using the following parameters:

http://app-server.space/weather_app/{city}/{period}

**Period can either be 'current' or 'forecast':**

*http://app-server.space/weather_app/london/current*

*http://app-server.space/weather_app/reading/forecast*

##### Bar/Line charts are accessible using the following parameters:

*http://app-server.space/weather_app/{city}/{period}/barchart*

*http://app-server.space/weather_app/{city}/{period}/linechart*

**Charts are only possible with forecast requests.*

## License

Weather data is pulled from Open Weather Map.