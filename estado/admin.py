from django.contrib import admin
from estado.models import Estado

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(Estado,EstadoAdmin)