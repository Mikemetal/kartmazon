from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from estado import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^estado/$', views.EstadosList.as_view()),
    url(r'^estado/(?P<pk>[0-9]+)/$', views.EstadosDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)