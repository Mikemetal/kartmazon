from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from usuariosperfil import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^usuariosperfil/$', views.UsuariosPerfilesList.as_view()),
    url(r'^usuariosperfil/(?P<pk>[0-9]+)/$', views.UsuariosPerfilDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)