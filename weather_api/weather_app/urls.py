from django.conf.urls import url

from weather_app import views

urlpatterns = [
    url(r'^(?P<filters>(?:/[^/]+/[^/]+)*)$', views.index, name='index'),
    url(r"^(?P<city>[^/]+)/$", views.profile),
    url(r"^(?P<city>[^/]+)/(?P<period>[^/]+)$", views.profile),
]