from django.db import models

# Create your models here.

class Area(models.Model):
    nombre = models.CharField(max_length=15)
    tamanio = models.CharField(max_length=15)
    ubicacion = models.CharField(max_length=15)
    maxi_person = models.CharField(max_length=15)
    estado = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombre
    
class Productos(models.Model):
    nombre = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    fecha_expiracion = models.CharField(max_length=15)
    peso = models.CharField(max_length=11)
    area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)

