from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from pour.drinks.models import Drinks, Ingredients

def home(request):
    mying = Ingredients.objects.all().values
    mydrinks = Drinks.objects.all().values
    template = loader.get_template('home.html')  
    context = {
        'mying' : mying,
        'mydrinks' : mydrinks
    }
    return HttpResponse(template.render(context, request))

def index(request):
    mydrinks = Drinks.objects.all().values
    template = loader.get_template('index.html')
    context = {
        'mydrinks' : mydrinks
    }
    return HttpResponse(template.render(context, request))