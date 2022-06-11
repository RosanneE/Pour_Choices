from django.contrib.postgres.fields import ArrayField
from django.db import models


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=200)
    ingredient_pk = models.CharField(max_length=300)
    ingredient_fk = models.CharField(max_length=300)
    ingredient_boo = models.BooleanField(True)
    ingredient_list = ArrayField(models.CharField(max_length=100), default = list)

    def __str__(self):
        return self.ingredient

    class Meta:
        ordering = ['ingredient']

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    drink_ingredients= ArrayField(models.CharField(max_length=100), default = list)
    garnishes = ArrayField(models.CharField(max_length=100), default = list)
    recipie = models.CharField(max_length=2000)
    glass = models.CharField(max_length=200)
    tools = ArrayField(models.CharField(max_length=100), default = list)
    tags = ArrayField(models.CharField(max_length=100), default = list)
    drink_pk = models.CharField(max_length=300)
    drink_fk = models.CharField(max_length=300)
    drink_string = models.CharField(max_length=200)
    drink_list = ArrayField(models.CharField(max_length=100), default = list)

    def __str__(self):
        return self.drink_name

    class Meta:
        ordering = ['drink_name']

class Lists(models.Model):
    list_title = models.CharField(max_length=300)
    list_descriptions = models.CharField(max_length=300)
    list_pk = models.CharField(max_length=300)
    list_fk = models.CharField(max_length=300)
    list_need_array = ArrayField(models.CharField(max_length=100), default = list)
    list_need_string = models.CharField(max_length=200)
    # many to many
    drink_in_list = models.ManyToManyField(Drinks)

    def __str__(self):
        return self.list_title
