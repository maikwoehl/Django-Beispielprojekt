# This also imports the include function
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('artikel.views',
    url(r'^(?P<article_id>\d+)/$', 'index'),
   # url(r'^(?p<podcast_id>\d+)/$', 'podcast'),
)
