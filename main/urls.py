from django.conf.urls import patterns, include, url 
from hideURL.main.views import *

urlpatterns = patterns('',
    (r'^$', 'hideURL.main.urls.hideURL'),
    (r'^(?P<md5sum>\w+)/$', 'hideURL.main.urls.hideURL'),
)

