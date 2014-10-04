from django.db import models
from ciudad.models import Ciudad
from paquetes.models import Paquetes

class Usuarios(models.Model):
    usuario = models.ForeignKey('auth.User', related_name='usuarios')
    ciudad = models.ForeignKey(Ciudad) # Field name made lowercase.
    paquetes = models.ForeignKey(Paquetes, blank=True, null=True) # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True) # Field name made lowercase.
    apellido = models.CharField(max_length=45, blank=True) # Field name made lowercase.
    vendedor = models.IntegerField(blank=True, null=True) # Field name made lowercase.

    def __unicode__(self):
        return self.usuario.username

    class Meta:
        db_table = 'Usuarios'
        verbose_name_plural = "Usuarios"