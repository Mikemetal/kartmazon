from django.db import models
import os
from django.contrib.auth.models import User
from vehiculos.models import Vehiculos


class Fotosvehiculos(models.Model):
    vehiculo = models.ForeignKey(Vehiculos, related_name="fotosvehiculos")
    path = models.ImageField(upload_to="/media", blank=True) # Field name made lowercase.

    class Meta:
        verbose_name_plural = "Fotosvehiculos"

    def __unicode__(self):
        return "%s" % (self.path)
