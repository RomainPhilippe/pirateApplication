# -*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

import numpy as np
import pandas as pd

from map.models import Area
from map.models import AreaHand
from django.core.serializers.json import DjangoJSONEncoder
import json

from map.forms import InputForm

def index(request):
    print "index"
    return HttpResponse("Hello, world. You're at the polls index.")


def date_actuelle(request):
    areas = Area.objects.all()  # Nous sélectionnons toutes nos zones
    return render(request, 'index.html', {'date': datetime.now(), 'list_area': areas})


def get_list_areas(request):
    # if request.method == 'POST':
    post_text = request.GET.get('email')
    print post_text
    response_data = {}

    areas = Area.objects.all().values_list('zone', 'min_lat')  # Nous sélectionnons toutes nos zones

    response_data['listReturn'] = areas

    return HttpResponse(
            json.dumps(list(areas), cls=DjangoJSONEncoder),
            content_type="application/json")

    # else:
    #    return HttpResponse(
    #        json.dumps({"nothing to see": "this isn't happening"}),
    #        content_type="application/json"
    #   )

    # return render(request, 'index.html', {'date': datetime.now(), 'list_area': areas})


def contact(request):
    params = []
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = InputForm(request.POST)  # Nous reprenons les données

        if form.is_valid():  # Nous vérifions que les données envoyées sont valides
            # Ici nous pouvons traiter les données du formulaire
            boatType = form.cleaned_data['boatType']
            month = form.cleaned_data['month']
            fortnight = form.cleaned_data['fortnight']
            activity = form.cleaned_data['activity']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True

            params = [boatType, month, fortnight, activity]

        else:
            print("pas valide mais ok")

    else:  # Si ce n'est pas du POST, c'est probablement une requête GET
        form = InputForm()  # Nous créons un formulaire vide

    date = datetime.now()

    areas = Area.objects.all().values_list('zone', 'min_lat', 'max_lat', 'min_lon',
                                           'max_lon')  # Nous sélectionnons toutes nos zones

    list_area = unicode(json.dumps(list(areas)))

    areasId = Area.objects.all().values_list('zone', flat=True)
    list_areasId = [entry for entry in areasId]

    get_datas(list_areasId, params)

    return render(request, 'index.html', locals())


def get_datas(list_areasId, params):
    size = len(list_areasId)

    maxYear = max(AreaHand.objects.all().values_list('year', flat=True))

    ColYears = np.repeat(maxYear + 1, size)
    ColArea = list_areasId
    if (len(params) > 3):
        ColMonth = np.repeat(params[1], size)
        ColFortnight = np.repeat(params[2], size)
        ColType = np.repeat(params[0], size)
        ColActivity = np.repeat(params[3], size)
    else:
        ColMonth = np.repeat(0, size)
        ColFortnight = np.repeat(0, size)
        ColType = np.repeat(0, size)
        ColActivity = np.repeat(0, size)

    dic = {'Years': ColYears, 'Month': ColMonth, 'Fortnight': ColFortnight, 'Area': ColArea, 'Type': ColType,
           'Activity': ColActivity}
    dfArea = pd.DataFrame(dic)
    print dfArea
    return dfArea
