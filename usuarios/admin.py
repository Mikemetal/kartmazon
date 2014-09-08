from django.contrib import admin
from usuarios.models import Usuarios

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'ciudad','paquetes','nombre','apellido','vendedor')

admin.site.register(Usuarios,UsuariosAdmin)