from django.db import models
from marca.models import Marca

class Modelo(models.Model):
    marca = models.ForeignKey(Marca,related_name="marca") # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True) # Field name made lowercase.

    def __unicode__(self):
        return self.nombre

    class Meta:
        db_table = 'Modelos'
        verbose_name_plural = "Modelos"