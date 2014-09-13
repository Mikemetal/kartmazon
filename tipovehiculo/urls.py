from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from tipovehiculo import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^tipovehiculo/$', views.TipovehiculosList.as_view()),
    url(r'^tipovehiculo/(?P<pk>[0-9]+)/$', views.TipovehiculoDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)