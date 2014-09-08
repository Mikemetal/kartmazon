from django.contrib import admin
from paquetes.models import Paquetes

class PaquetesAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','precio')

admin.site.register(Paquetes,PaquetesAdmin)