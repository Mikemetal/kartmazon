# import os, sys
# os.environ['DJANGO_SETTINGS_MODULE'] = 'kartmazon.settings'
from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from vehiculos import views
admin.autodiscover()

router = routers.DefaultRouter()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kartmazon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^', include('vehiculos.urls')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
)

# if __name__ == '__main__':
#
#     from django.core.urlresolvers import RegexURLPattern, RegexURLResolver
#     from django.utils.termcolors import colorize
#
#     sys.path.append(os.path.abspath('..'))
#     os.environ['DJANGO_SETTINGS_MODULE'] = 'kartmazon.settings'
#
#     def traverse(url_patterns, prefix=''):
#         for p in url_patterns:
#             if isinstance(p, RegexURLPattern):
#                 composed = '%s%s' % (prefix, p.regex.pattern)
#                 composed = composed.replace('/^', '/')
#                 print colorize('\t%s' % (composed), fg='green'), '==> ',
#                 try:
#                     sys.stdout.write(colorize('%s.' % p.callback.__module__,
#                         fg='yellow'))
#                     print p.callback.func_name
#                 except:
#                     print p.callback.__class__.__name__
#             if isinstance(p, RegexURLResolver):
#                 traverse(p.url_patterns, prefix=p.regex.pattern)
#
#     traverse(urlpatterns)