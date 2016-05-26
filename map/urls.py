from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.result, name='date'),
    url(r'^cluster$', views.getCluster, name='cluster'),
    url(r'^list_area$', views.get_list_areas, name='areas'),
    url(r'^result/$', views.result),

]
