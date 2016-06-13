from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^prediction$', views.resultPrediction, name='date'),
    url(r'^cluster$', views.getCluster, name='cluster'),
]
