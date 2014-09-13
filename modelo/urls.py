from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from modelo import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^modelo/$', views.ModelosList.as_view()),
    url(r'^modelo/(?P<pk>[0-9]+)/$', views.ModelosDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)