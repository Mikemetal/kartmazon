from django.db import models
from vehiculos.models import Vehiculos

class Fotosvehiculos(models.Model):
    vehiculo = models.ForeignKey(Vehiculos, related_name="fotosvehiculos")
    path = models.CharField(max_length=45, blank=True) # Field name made lowercase.

    class Meta:
        verbose_name_plural = "Fotosvehiculos"

    def __unicode__(self):
        return "%s - %s" % (self.vehiculo,self.path)