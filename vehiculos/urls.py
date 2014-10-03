from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from vehiculos import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^vehiculo/$', views.VehiculosListAdd.as_view()),
    url(r'^listvehiculo/$', views.VehiculosList.as_view()),
    url(r'^vehiculo/(?P<pk>[0-9]+)/$', views.VehiculosDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)