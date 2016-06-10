
from django.conf.urls import include, url
from django.contrib import admin
from map import views

urlpatterns = [
    url(r'^map/', include('map.urls')),
    url(r'^admin/', admin.site.urls),
]