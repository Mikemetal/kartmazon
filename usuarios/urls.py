from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from usuarios import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^usuarios/$', views.UserList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)