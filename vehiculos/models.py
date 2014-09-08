from __future__ import unicode_literals
from django.db import models
from modelo.models import Modelo
from tipovehiculo.models import Tipovehiculo

class Vehiculos(models.Model):
    usuario = models.ForeignKey('auth.User', related_name='usuario') # Field name made lowercase.
    modelo = models.ForeignKey(Modelo,related_name='modelo') # Field name made lowercase.
    tipovehiculo = models.ForeignKey(Tipovehiculo,related_name='tipovehiculo') # Field name made lowercase.
    precio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True) # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True) # Field name made lowercase.
    kilometraje = models.IntegerField(blank=True, null=True) # Field name made lowercase.
    contador = models.IntegerField(blank=True, null=True) # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

