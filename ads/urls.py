from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from ads import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^ads/$', views.AdsList.as_view()),
    url(r'^ads/(?P<pk>[0-9]+)/$', views.AdsDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)