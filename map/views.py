#-*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

from map.models import Area
from django.core.serializers.json import DjangoJSONEncoder
import json

def index(request):
    print "index"
    return HttpResponse("Hello, world. You're at the polls index.")

def date_actuelle(request):

    areas = Area.objects.all() # Nous sélectionnons toutes nos zones
    return render(request, 'index.html', {'date': datetime.now(), 'list_area': areas})



def get_list_areas(request):

    print "get_list_areas"

    #if request.method == 'POST':
    #post_text = request.POST.get('the_post')
    response_data = {}

    areas = Area.objects.all().values_list('zone', 'min_lat') # Nous sélectionnons toutes nos zones

    print type(areas)
    response_data['listReturn'] = areas

    return HttpResponse(
            json.dumps(list(areas), cls=DjangoJSONEncoder),
            content_type="application/json")

    #else:
    #    return HttpResponse(
    #        json.dumps({"nothing to see": "this isn't happening"}),
    #        content_type="application/json"
    #   )

    #return render(request, 'index.html', {'date': datetime.now(), 'list_area': areas})