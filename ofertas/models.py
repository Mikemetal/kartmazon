from django.db import models
from vehiculos.models import Vehiculos


class Ofertas(models.Model):
    vehiculo = models.ForeignKey(Vehiculos, related_name='vehiculos')
    usuario = models.ForeignKey('auth.User', related_name='ofertas') # Field name made lowercase.
    oferta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    contraoferta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True) # Field name made lowercase.

    class Meta:
        verbose_name_plural = "Ofertas"