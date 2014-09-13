from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from marca import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^marca/$', views.MarcasList.as_view()),
    url(r'^marca/(?P<pk>[0-9]+)/$', views.MarcasDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)