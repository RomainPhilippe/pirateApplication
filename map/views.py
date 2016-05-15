#-*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

from map.models import Area
from django.core.serializers.json import DjangoJSONEncoder
import json

#from map.forms import InputForm
from map.forms import ContactForm


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

#def choose(request):
#    if request.method == 'POST':  # S'il s'agit d'une requête POST
#       form = InputForm(request.POST)  # Nous reprenons les données

#        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
#            boatType = form.cleaned_data['boatType']
            #fortnight = form.cleaned_data['fortnight']
            #piratingActivity = form.cleaned_data['piratingActivity']
            #clusteringType = form.cleaned_data['ChoiceField']

#    else: # Si ce n'est pas du POST, c'est probablement une requête GET
#        form = InputForm()  # Nous créons un formulaire vide

#    return render(request, 'index.html', locals())


def contact(request):
    print "views.CONTACT"

    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm(request.POST)  # Nous reprenons les données
        print("POST.CONTACT")

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            print "if.views.CONTACT"
            # Ici nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True
        else:
            print("pas valide mais ok")

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        print "else.views.CONTACT"
        form = ContactForm()  # Nous créons un formulaire vide

    print("return")

    return render(request, 'index.html', locals())
