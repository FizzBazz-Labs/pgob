from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=150)


class Nationality(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
