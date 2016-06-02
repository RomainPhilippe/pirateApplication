from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^prediction$', views.resultPrediction, name='date'),
    url(r'^cluster$', views.getCluster, name='cluster'),
]
