from django.contrib import admin
from ads.models import Ads

class AdsAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')

admin.site.register(Ads,AdsAdmin)