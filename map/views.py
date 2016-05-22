# -*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier

from map.models import Area
from map.models import AreaHand
from django.core.serializers.json import DjangoJSONEncoder
import json

from map.forms import InputForm

def index(request):
    print "index"
    return HttpResponse("Hello, world. You're at the polls index.")

#############################################################################
#############################################################################
# ML function
def bool_attack(count):
    if count>0:
        return 1
    else:
        return 0


def binaryColumn(df,uniqueArea,uniqueType):
    featureBinary=[]
    for i in range(0,len(uniqueArea)):
        nameColArea='area_'+str(uniqueArea[i])
        df[nameColArea]=0
        featureBinary.append(nameColArea)
    for i in range(0,len(uniqueType)):
        nameColType='type_'+str(uniqueType[i])
        df[nameColType]=0
        featureBinary.append(nameColType)


    for index, row in df.iterrows():
        df.set_value(index, "area_"+str(row['area']),1)
        df.set_value(index, "type_"+str(row['boatType']),1)


    return df,featureBinary



def getPrediction(dfTrain,dfTest,features,target,nb_esti=250,nb_features=1):
    model = RandomForestClassifier(random_state=1,n_estimators=nb_esti,max_features=nb_features)
    model=model.fit(dfTrain[features], dfTrain[target])
    predictions=model.predict(dfTest[features])
    probabilities=model.predict_proba(dfTest[features])[:, 1]
    return predictions,probabilities

#############################################################################
#############################################################################


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
    # sélections des zones
    areas = Area.objects.all().values_list('zone', 'min_lat', 'max_lat', 'min_lon', 'max_lon')

    array2d=np.asarray(list(areas))

    list_area = json.dumps(array2d.tolist())

    areasId = Area.objects.all().values_list('zone', flat=True)
    list_areasId = [entry for entry in areasId]

    if request.method == 'POST':
        # S'il s'agit d'une requête POST
        form = InputForm(request.POST)
        # Nous reprenons les données

        if form.is_valid():
            # Nous vérifions que les données envoyées sont valides
            # Ici nous pouvons traiter les données du formulaire
            boatType = form.cleaned_data['boatType']
            month = form.cleaned_data['month']
            fortnight = form.cleaned_data['fortnight']
            activity = form.cleaned_data['activity']

            envoi = True
            params = [boatType, month, fortnight, activity]
            dfTest=get_datas(list_areasId, params)
            predict,probabilities=getTabPrediction(dfTest)

            p = np.column_stack( [ array2d , probabilities ] )
            list_area = json.dumps(p.tolist())

        else:
            print("pas valide mais ok")

    else:
        # Si ce n'est pas du POST, c'est probablement une requête GET
        form = InputForm()
        # Nous créons un formulaire vide

    date = datetime.now()
    print type(list_area)
    print list_area

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

    # creation test dataframe in order to get predicions
    dic = {'year': ColYears, 'month': ColMonth, 'fortnight': ColFortnight, 'area': ColArea, 'boatType': ColType,
           'activity': ColActivity}
    dfTest = pd.DataFrame(dic)

    return dfTest


def getTabPrediction(dfTest):
    # we get train dataframe from database
    dfAreaHand = pd.DataFrame(list(AreaHand.objects.all().values()))
    dfAreaHand['attack'] = dfAreaHand.apply(lambda row: bool_attack(row['count']), axis=1)


    # transformations ...
    uniqueArea=dfAreaHand["area"].unique()
    uniqueType=dfAreaHand["boatType"].unique()

    dfAreaHand,featureBinary=binaryColumn(dfAreaHand,uniqueArea,uniqueType)
    dfTest,featureBinary=binaryColumn(dfTest,uniqueArea,uniqueType)


    # Columns important for the ML machine learning
    features=['activity','fortnight','month','year']
    features=np.concatenate([features,featureBinary]).tolist()
    target='attack'

    print features

    print "Train dataset : "
    print dfAreaHand.head()

    print "dfTest : "
    print dfTest.head()

    predictions,probabilities=getPrediction(dfAreaHand,dfTest,features,target)
    print predictions
    print type(predictions)
    print probabilities
    print type(probabilities)

    return predictions,probabilities

