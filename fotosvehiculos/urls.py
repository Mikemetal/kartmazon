from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from fotosvehiculos import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^fotosvehiculos/$', views.FotosvehiculosList.as_view()),
    url(r'^fotosvehiculos/(?P<pk>[0-9]+)/$', views.FotosvehiculosDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)