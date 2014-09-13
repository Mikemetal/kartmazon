from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from paquetes import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^paquetes/$', views.PaquetesList.as_view()),
    url(r'^paquetes/(?P<pk>[0-9]+)/$', views.PaquetesDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)