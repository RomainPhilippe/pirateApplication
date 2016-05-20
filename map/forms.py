#-*- coding: utf-8 -*-

from django import forms
from map.models import AreaHand

import pandas as pd
import numpy as np

class InputForm(forms.Form):
    dbTypes = AreaHand.objects.all().values_list('boatType', flat=True)
    list_dbTypes = [entry for entry in dbTypes]
    dicBoat = {'Boats': list_dbTypes}
    dfArea = pd.DataFrame(dicBoat)
    dfArea=dfArea['Boats'].unique()
    listTuples = []
    for i in range(0, len(dfArea)):
        listTuples.append(tuple([str(i+1),dfArea[i]]))

    boatType = forms.ChoiceField(label='Type de bateau', choices=listTuples)
    CHOICES = (('1','Janvier'),('2','Février'), ('3','Mars'), ('4','Avril'), ('5','Mai'), ('6','Juin'), ('7','Juillet'), ('8','Août'), ('9','Septembre'), ('10','Octobre'), ('11','Novembre'), ('12','Décembre'))
    month = forms.ChoiceField(label='Mois', choices=CHOICES)
    CHOICES2 = (('1', 'Première quinzaine',), ('2', 'Seconde quinzaine',))
    fortnight = forms.ChoiceField(label='Quinzaine', widget=forms.RadioSelect, choices=CHOICES2)
    CHOICES3 = (('2', 'Forte activité',), ('1', 'Faible activité',))
    activity = forms.ChoiceField(label='Activité', widget=forms.RadioSelect, choices=CHOICES3)

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)