from ast import Return
import random
import re
from typing import List
from urllib import request
from venv import create
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import DetailView
from django.urls import reverse
from pickle import NONE
from drinks.models import Drinks, Ingredients, Lists

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        # Get gets search param
        name = self.request.GET.get("ingredient")
        my_menu = MyMenu()
        # my_menu = 'broken'
        #MyMenu()
        print(my_menu)
        context['my_menu'] = my_menu
        # If param, will filter by param
        if name != None:
            context['ingredients'] = Ingredients.objects.filter(ingredient__icontains=name).values()
            context['drinks'] = Drinks.objects.all().values()
            context["header"] = f'Ingredients containing "{name}"'
        else:
            context['ingredients'] = Ingredients.objects.all().values()
            context['drinks'] = Drinks.objects.all().values()
            context["header"] = "Ingredients"
        return context

class Index(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        # Get gets search param
        name = self.request.GET.get("drink_name")
        curr_rand_drink =RandomNumber()
        context['curr_rand_drink'] = curr_rand_drink
        if name != None:
            context['drinks'] = Drinks.objects.filter(drink_name__icontains=name).values()
            context["headerC"] = f'Cocktails containing "{name}"'
        else:
            context['drinks'] = Drinks.objects.all().values()
        return context

class DrinksCreate(CreateView):
    model = Drinks
    fields = ['drink_name','drink_ingredients', 'recipie', 'glass', 'tags']
    template_name = 'create_cocktail.html'
    def get_success_url(self):
        return reverse('cocktail_show', kwargs={'pk': self.object.pk})

class ListCreate(CreateView):
    model = Lists
    fields = ['list_title','list_descriptions']
    template_name = 'list_create.html'
    def get_success_url(self):
        return reverse('list_show', kwargs={'pk': self.object.pk})

class CocktailShow(DetailView):
    model = Drinks
    template_name = 'cocktail_show.html'
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        curr_rand_drink =RandomNumber()
        context['curr_rand_drink'] = curr_rand_drink
        return context

class ListShow(DetailView):
    model = Lists
    template_name = 'list_show.html'
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        curr_rand_drink =RandomNumber()
        context['curr_rand_drink'] = curr_rand_drink
        return context

class CocktailUpdate(UpdateView):
    model = Drinks
    fields = ['drink_name','drink_ingredients', 'recipie', 'glass', 'tags']
    template_name = 'cocktail_update.html'
    def get_success_url(self):
        return reverse('cocktail_show', kwargs={'pk': self.object.pk})
    
class ListUpdate(UpdateView):
    model = Lists
    fields = ['list_title','list_descriptions']
    template_name = 'list_update.html'
    def get_success_url(self):
        return reverse('list_show', kwargs={'pk': self.object.pk})

class MyPage(TemplateView):
    template_name = "my_page.html"
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['lists'] = Lists.objects.all().values()
        curr_rand_drink =RandomNumber()
        context['curr_rand_drink'] = curr_rand_drink
        return context

class About(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        curr_rand_drink =RandomNumber()
        context['curr_rand_drink'] = curr_rand_drink
        return context

def ListDelete(request,id):
    list = Lists.objects.get(id=id)
    list.delete()
    return HttpResponseRedirect(reverse('my_page'))

def IngredientUpdate(request, id):
    update = Ingredients.objects.get(id=id)
    print(update)
    print(update.ingredient_boo)
    if update.ingredient_boo == False:
        update.ingredient_boo = True
        update.save()
    else:
        update.ingredient_boo = False 
        update.save()
    print(update)   
    print(update.ingredient_boo)
    return HttpResponseRedirect(reverse('home'))


def ing_search(request):
    mying = Ingredients.objects.filter(ingredient__icontains='i').values
    template = loader.get_template('ing_search.html') 
    curr_rand_drink =RandomNumber()
    context = {  
        'curr_rand_drink' : curr_rand_drink,
        'mying' : mying,
    }
    return HttpResponse(template.render(context, request))

def RandomNumber():
    var = list(Drinks.objects.all())
    rand_drink = random.sample(var,1)
    return(int(rand_drink[0].id))

    
def MyMenu():
    my_menu = []
    i=0
    j = 0
    my_ing = Ingredients.objects.filter(ingredient_boo=True)
    my_drinks = Drinks.objects.all()

    for drink in my_drinks:
        for each in my_drinks:
            if CreateArrays(drink)== True:
                my_menu.append(each.drink_name)                
        if not my_menu:
            my_menu.append('No Matches Found')
        print(my_menu)
        return(my_menu)

# Compaires array to sub array, returns True or False
def CreateArrays(drink):
    array = [] 
    sub = []
    i=0
    # print(my_ing)
    # create an array list of my ingredients
    for each in Ingredients.objects.all():
        if each.ingredient_boo == True:
            array.append(each.ingredient)
    # print(array)
    # create an array list of drink ingredients
    for each in drink.drink_ingredients:
         sub.append(each)
    CheckArrays(array, sub, each, i)

# Compaires array to sub array, returns True or False
def CheckArrays(array, sub, each, i):
    match=[]
    j=0
    #compare each item in sub array to array items, if all items are contained return true, else return false
            # match.append(each)
    print(f'each = {each}')
    print(f'array[j] = {array[i]}')
    # while  i < (len(sub)-1):
    #     for each in array:
    #         # print(array[j])
    #         if each == array[j]:
    #             match.append(each)
    #             if i<(len(array)-1):
    #                 i= i+1
    #                 j = j+1
    #             else:
    #                 j=j+1
    #         if not match:
    #             print("no match")
    #             return False
    #         else:
    #             print(match)
    #             print(each)
    #             if len(match) == len(each):
    #                 return True
    #             else:
    #                 return False