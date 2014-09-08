from django.db import models
from estado.models import Estado

class Ciudad(models.Model):
    estado = models.ForeignKey(Estado) # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True) # Field name made lowercase.

    def __unicode__(self):
        return self.nombre