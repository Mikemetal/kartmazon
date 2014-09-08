from django.contrib import admin
from modelo.models import Modelo

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'nombre')

admin.site.register(Modelo,ModeloAdmin)