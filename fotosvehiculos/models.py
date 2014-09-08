from django.db import models
from vehiculos.models import Vehiculos

class Fotosvehiculos(models.Model):
    vehiculo = models.ForeignKey(Vehiculos)
    path = models.CharField(max_length=45, blank=True) # Field name made lowercase.