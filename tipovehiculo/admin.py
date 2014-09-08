from django.contrib import admin
from tipovehiculo.models import Tipovehiculo

class TipovehiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(Tipovehiculo,TipovehiculoAdmin)