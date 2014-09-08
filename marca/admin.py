from django.contrib import admin
from marca.models import Marca

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Marca,MarcaAdmin)