from django.db import models
from django.db.models.base import Model

class Place(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    yes = models.PositiveIntegerField(default=0)
    no = models.PositiveIntegerField(default=0)

class User(models.Model):
    pass


