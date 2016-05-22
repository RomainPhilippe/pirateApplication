from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # url(r'^$', views.date_actuelle,name='date'),
    url(r'^$', views.result, name='date'),
    url(r'^list_area$', views.get_list_areas, name='areas'),
    # url(r'^choose/$', views.choose),
    url(r'^result/$', views.result),

]
