from typing import List
from django.contrib import admin
from .models import Ingredients, Drinks, Lists
# Register your models here.
admin.site.register(Ingredients)
admin.site.register(Drinks)
admin.site.register(Lists)