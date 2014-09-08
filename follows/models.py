from django.db import models
from vehiculos.models import Vehiculos

class Follows(models.Model):
    usuario = models.ForeignKey('auth.User', related_name='follows') # Field name made lowercase.
    vehiculo = models.ForeignKey(Vehiculos)