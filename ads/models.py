from django.db import models

class Ads(models.Model):
    descripcion = models.CharField(max_length=45, blank=True) # Field name made lowercase.

    def __unicode__(self):
        return self.descripcion

    class Meta:
        db_table = 'Ads'
        verbose_name_plural = "Ads"