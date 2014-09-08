from django.contrib import admin
from ciudad.models import Ciudad

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado','nombre')

admin.site.register(Ciudad,CiudadAdmin)