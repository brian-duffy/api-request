# -*- coding: utf-8 -*-
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart


def get_bar_chart(data=None):
    """
    Function to return a chart object for rendering in a view
    :param data:
    :return:
    """
    all_temps = [x['main']['temp'] for i, x in(enumerate(data['list']))]
    all_dates = [x['dt_txt'][0:10] for i, x in(enumerate(data['list']))]
    bar_chart = [['Day', 'Temperature°C']]
    bar_chart.extend([all_dates[i], all_temps[i]] for i, x in enumerate(all_dates))
    # DataSource object
    data_source = SimpleDataSource(data=bar_chart)
    # Chart object
    chart = LineChart(data_source)
    return chart