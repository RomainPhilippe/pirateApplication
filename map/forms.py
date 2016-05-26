# -*- coding: utf-8 -*-

from django import forms
from map.models import AreaHand

import pandas as pd


class InputForm(forms.Form):
    # creation of the boat type list according to the values contained in the BDD
    dbTypes = AreaHand.objects.all().values_list('boatType', flat=True)
    list_dbTypes = [entry for entry in dbTypes]
    dicBoat = {'Boats': list_dbTypes}
    dfArea = pd.DataFrame(dicBoat)
    dfArea = dfArea['Boats'].unique()
    listTuples = []
    for i in range(0, len(dfArea)):
        listTuples.append(tuple([dfArea[i], dfArea[i]]))

    # boat types
    boatType = forms.ChoiceField(label='Type de bateau', choices=listTuples)
    # month
    CHOICES = (
    ('1', 'Janvier'), ('2', 'Février'), ('3', 'Mars'), ('4', 'Avril'), ('5', 'Mai'), ('6', 'Juin'), ('7', 'Juillet'),
    ('8', 'Août'), ('9', 'Septembre'), ('10', 'Octobre'), ('11', 'Novembre'), ('12', 'Décembre'))
    month = forms.ChoiceField(label='Mois', choices=CHOICES)
    # fortnight
    CHOICES2 = (('1', 'Première quinzaine',), ('2', 'Seconde quinzaine',))
    fortnight = forms.ChoiceField(label='Quinzaine', choices=CHOICES2)
    # activity level
    CHOICES3 = (('1', 'Faible activité',), ('2', 'Forte activité',))
    activity = forms.ChoiceField(label='Activité', choices=CHOICES3)

class InputFormCluster(forms.Form):
    # creation of the boat type list according to the values contained in the BDD
    #dbTypes = AreaHand.objects.all().values_list('boatType', flat=True)
    #list_dbTypes = [entry for entry in dbTypes]
    #dicBoat = {'Boats': list_dbTypes}
    #dfArea = pd.DataFrame(dicBoat)
    #dfArea = dfArea['Boats'].unique()
    #listTuples = []
    #for i in range(0, len(dfArea)):
    #    listTuples.append(tuple([dfArea[i], dfArea[i]]))

    # boat types
    #boatType = forms.ChoiceField(label='Type de bateau', choices=listTuples)

    # month
    CHOICES = (
        ('1', 'Janvier'), ('2', 'Février'), ('3', 'Mars'), ('4', 'Avril'), ('5', 'Mai'), ('6', 'Juin'), ('7', 'Juillet'),
        ('8', 'Août'), ('9', 'Septembre'), ('10', 'Octobre'), ('11', 'Novembre'), ('12', 'Décembre'))
    month = forms.ChoiceField(label='Mois', choices=CHOICES)
    # years
    CHOICES_YEARS = (('2008', '2008'), ('2009', '2009'),('2010', '2010'),('2011', '2011'),('2012', '2012'),('2013', '2013'),('2014', '2014'))
    years = forms.ChoiceField(label='Année', choices=CHOICES_YEARS)
