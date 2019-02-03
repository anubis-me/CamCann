from django.contrib import admin
from . import views
from django.conf.urls import url
 #/collector/
urlpatterns = [
    url('^$', views.index, name='index'),
#/collector/71/
    url(r'^(?P<data_id>[0-9]+)', views.detail, name='detail')
]

