from django.contrib import admin
from follows.models import Follows

class FollowsAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario','vehiculo')

admin.site.register(Follows,FollowsAdmin)