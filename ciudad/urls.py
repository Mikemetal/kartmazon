from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from ciudad import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^ciudad/$', views.CiudadesList.as_view()),
    url(r'^ciudad/(?P<pk>[0-9]+)/$', views.CiudadesDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)