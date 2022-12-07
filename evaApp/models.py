from django.db import models
from primeraapp.models import Area


# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField(max_length=20)
    rut = models.CharField(max_length=13)
    cargo = models.CharField(max_length=25)
    fono = models.CharField(max_length=9)
    area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)

    
