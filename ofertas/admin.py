from django.contrib import admin
from ofertas.models import Ofertas

class OfertasAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehiculo','usuario','oferta','contraoferta')

admin.site.register(Ofertas,OfertasAdmin)