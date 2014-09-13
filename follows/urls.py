from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from follows import views

urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^follows/$', views.FollowsList.as_view()),
    url(r'^follows/(?P<pk>[0-9]+)/$', views.FollowsDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)