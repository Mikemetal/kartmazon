from django.contrib import admin
from usuariosperfil.models import Usuariosperfil

class UsuariosperfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario','pathlogo','descripcion')

admin.site.register(Usuariosperfil,UsuariosperfilAdmin)