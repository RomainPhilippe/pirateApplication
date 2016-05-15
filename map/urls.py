from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.date_actuelle,name='date'),
    url(r'^list_area$', views.get_list_areas,name='areas'),
]