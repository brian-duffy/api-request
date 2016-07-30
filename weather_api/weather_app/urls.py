from django.conf.urls import url
from django.views.generic import RedirectView
from weather_app import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='https://github.com/brian-duffy/yoyo-test/blob/master/README.md')),
    url(r"^(?P<city>[^/]+)/$", views.web_api),
    url(r"^(?P<city>[^/]+)/(?P<period>[^/]+)/$", views.web_api),
    url(r"^(?P<city>[^/]+)/(?P<period>[^/]+)/(?P<bar_chart>[^/]+)/$", views.web_api),
]