from django.db import models

class Estado(models.Model):
    nombre = models.CharField(max_length=45, blank=True) # Field name made lowercase.

    def __unicode__(self):
        return self.nombre

    class Meta:
        db_table = 'Estados'
        verbose_name_plural = "Estados"