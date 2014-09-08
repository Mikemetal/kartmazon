from django.db import models

class Usuariosperfil(models.Model):
    usuario = models.ForeignKey('auth.User', related_name='usuariosperfil') # Field name made lowercase.
    pathlogo = models.CharField(max_length=45, blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True) # Field name made lowercase.
