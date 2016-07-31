# -*- coding: utf-8 -*-
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart, BarChart


def get_chart(data=None, chart='barchart'):
    """
    Function to return a chart object for rendering in a view
    :param data:
    :return:
    """
    all_temps = [x['main']['temp'] for i, x in(enumerate(data['list']))]
    all_dates = [x['dt_txt'][0:10] for i, x in(enumerate(data['list']))]
    _chart = [['Day', 'Temperature°C']]
    _chart.extend([all_dates[i], all_temps[i]] for i, x in enumerate(all_dates))
    # DataSource object
    data_source = SimpleDataSource(data=_chart)
    # Chart object
    if chart == 'barchart':
        chart = BarChart(data_source)
    else:
        chart = LineChart(data_source)
    return chart
