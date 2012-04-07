# This also imports the include function
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from blog.feeds import ArticlesFeed, PodcastFeed

feeds = {
    'articles': ArticlesFeed,
    'podcast': PodcastFeed,
}

urlpatterns = patterns('artikel.views',
    url(r'^(?P<article_id>\d+)/$', 'index'),
    
    url(r'^tagged/(?P<tag_id>.*)/$', 'tagged'),
    
    
   # url(r'^(?p<podcast_id>\d+)/$', 'podcast'),
)

urlpatterns += patterns('',
	
    # Feeds
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
	
)
