from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from drinks.models import Drinks, Ingredients

def home(request):
    mying = Ingredients.objects.all().values
    mydrinks = Drinks.objects.all().values
    template = loader.get_template('home.html')  
    context = {
        'mying' : mying,
        'mydrinks' : mydrinks
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({},request))


def ing_search(request):
    mying = Ingredients.objects.filter(ingredient__icontains='i').values
    template = loader.get_template('ing_search.html')  
    context = {
        'mying' : mying,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    mydrinks = Drinks.objects.all().values
    template = loader.get_template('index.html')
    context = {
        'mydrinks' : mydrinks
    }
    return HttpResponse(template.render(context, request))

