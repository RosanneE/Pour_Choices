from operator import imod
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=200)

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    drink_ingredients= ArrayField(models.CharField(max_length=100), default = [])
    garnishes = ArrayField(models.CharField(max_length=100), default = [])
    directions= models.CharField(max_length=2000)
    glass = models.CharField(max_length=200)
    tools = ArrayField(models.CharField(max_length=100), default = [])
    tags = ArrayField(models.CharField(max_length=100), default = [])

