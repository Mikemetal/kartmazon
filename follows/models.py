from django.db import models
from vehiculos.models import Vehiculos

class Follows(models.Model):
    usuario = models.ForeignKey('auth.User', related_name='usuario_usuario') # Field name made lowercase.
    vehiculo = models.ForeignKey(Vehiculos, related_name='vehiculo_vehiculo')

    class Meta:
        db_table = 'Follows'
        verbose_name_plural = "Follows"