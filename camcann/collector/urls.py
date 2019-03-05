from django.contrib import admin
from . import views
from django.conf.urls import url
urlpatterns = [
    url('^$', views.index, name='index'),
    #url(r'^(?P<data_id>[0-9]+)', views.detail, name='detail'),
    url(r'^create/', views.data_create_view, name='create'),
    url(r'^indexdata',views.index_graphs),
    url(r'^colors',views.colors),
    url(r'^target_api',views.target_api),
    url(r'^tag_data',views.tag_data)
]

