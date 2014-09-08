from django.db import models

class Paquetes(models.Model):
    nombre = models.CharField(max_length=45, blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True) # Field name made lowercase.
    precio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True) # Field name made lowercase.
