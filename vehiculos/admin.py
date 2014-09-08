from django.contrib import admin
from vehiculos.models import Vehiculos

class VehiculosAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'modelo','tipovehiculo','precio','descripcion','year','kilometraje','contador','created_at','modified_at')

admin.site.register(Vehiculos,VehiculosAdmin)