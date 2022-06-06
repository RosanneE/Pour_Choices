from multiprocessing import context
from pickle import NONE
from unicodedata import name
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import DetailView
from django.urls import reverse

from drinks.models import Drinks, Ingredients

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        # Get gets search param
        name = self.request.GET.get("ingredient")
        # If param, will filter by param
        if name != None:
            context['ingredients'] = Ingredients.objects.filter(ingredient__icontains=name).values()
            context["header"] = f'Ingredients containing "{name}"'
        else:
            context['ingredients'] = Ingredients.objects.all().values()
            context["header"] = "Ingredients"
        return context

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        # Get gets search param
        name = self.request.GET.get("drink_name")
        if name != None:
            context['drinks'] = Drinks.objects.filter(drink_name__icontains=name).values()
            context["headerC"] = f'Cocktails containing "{name}"'
        else:
            context['drinks'] = Drinks.objects.all().values()
        return context

class DrinksCreate(CreateView):
    model = Drinks
    fields = ['drink_name','drink_ingredients']
    template_name = 'createCocktail.html'
    success_url = '/create/'

class CocktailShow(DetailView):
    model = Drinks
    template_name = 'cocktail_show'

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



