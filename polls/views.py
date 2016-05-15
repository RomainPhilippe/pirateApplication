from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    print "index"
    return HttpResponse("Hello, world. You're at the polls index.")

def date_actuelle(request):
    print "date_actuelle"
    return render(request, 'index.html', {'date': datetime.now()})