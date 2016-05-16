#-*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

import numpy as np

from map.models import Area
from django.core.serializers.json import DjangoJSONEncoder
import json

from map.forms import InputForm
#from map.forms import ContactForm


def index(request):
    print "index"
    return HttpResponse("Hello, world. You're at the polls index.")

def date_actuelle(request):

    areas = Area.objects.all() # Nous sélectionnons toutes nos zones
    return render(request, 'index.html', {'date': datetime.now(), 'list_area': areas})



def get_list_areas(request):


    #if request.method == 'POST':
    post_text = request.GET.get('email')
    print post_text
    response_data = {}

    areas = Area.objects.all().values_list('zone', 'min_lat') # Nous sélectionnons toutes nos zones


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


def contact(request):

    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = InputForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            # Ici nous pouvons traiter les données du formulaire
            boatType = form.cleaned_data['boatType']
            month = form.cleaned_data['month']
            fortnight = form.cleaned_data['fortnight']
            activity = form.cleaned_data['activity']

            print "boat type : "+str(boatType)
            print "month : "+str(month)
            print "fortnight : "+str(fortnight)
            print "activity : "+str(activity)

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True
        else:
            print("pas valide mais ok")

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = InputForm()  # Nous créons un formulaire vide

    date=datetime.now()

    areas = Area.objects.all().values_list('zone', 'min_lat','max_lat','min_lon','max_lon') # Nous sélectionnons toutes nos zones
    list_area=unicode(json.dumps(list(areas)))

    #list_area=[['A', 14.842, 16.049, 41.22, 42.47]]
    print "list_area", list_area
    print "type(list_area)", type(list_area)
    return render(request, 'index.html', locals())
