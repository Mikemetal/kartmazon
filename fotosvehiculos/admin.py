from django.contrib import admin
from fotosvehiculos.models import Fotosvehiculos

class FotosvehiculosAdmin(admin.ModelAdmin):
    list_display = ('id','vehiculo','path')

admin.site.register(Fotosvehiculos,FotosvehiculosAdmin)