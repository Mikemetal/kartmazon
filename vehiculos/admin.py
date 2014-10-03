from django.contrib import admin
from vehiculos.models import Vehiculos

class VehiculosAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario','nombre_marca','modelo','tipovehiculo','precio','descripcion','year','kilometraje','contador','created_at','modified_at')

    def nombre_marca(self,obj):
        return obj.modelo.marca.nombre

    nombre_marca.short_description = "Marca"

admin.site.register(Vehiculos,VehiculosAdmin)