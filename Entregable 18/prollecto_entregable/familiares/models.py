from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    altura = models.FloatField()
    casado = models.BooleanField()
    edad = models.IntegerField()