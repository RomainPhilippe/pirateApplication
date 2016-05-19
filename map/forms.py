#-*- coding: utf-8 -*-

from django import forms

class InputForm(forms.Form):
    # TODO : récupérer les types de bateaux dans la base
    CHOICES = (('1','Carrier'),('2','Tanker'), ('3','Ro-Ro'))
    boatType = forms.ChoiceField(choices=CHOICES)
    month = forms.IntegerField()
    CHOICES2 = (('1', 'Première quinzaine',), ('2', 'Seconde quinzaine',))
    fortnight = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES2)
    CHOICES3 = (('1', 'Forte activité',), ('2', 'Faible activité',))
    activity = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES3)

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)