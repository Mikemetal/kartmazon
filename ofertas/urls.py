from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from ofertas import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^ofertas/$', views.OfertasList.as_view()),
    url(r'^ofertas/(?P<pk>[0-9]+)/$', views.OfertasDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)