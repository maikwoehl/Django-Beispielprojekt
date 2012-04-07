from artikel.models import Artikel, Podcast
from django.contrib.syndication.views import Feed
from django.utils import feedgenerator

class ArticlesFeed(Feed):
    feed_type = feedgenerator.Rss201rev2Feed
    title = "MyFeed"
    link = "/artikel/"
    description = "A small Feed"
 
    def items(self):
        return Artikel.objects.order_by('-art_pub_date')

    def item_link(self, item):
        return item.get_absolute_url()

    def item_categories(self,item):
		tags_list = item.get_categories()
		tags = tags_list.split(",")
		return tags
        
    def item_description(self,item):
        return item.get_description()

class PodcastFeed(Feed):
    feed_type = feedgenerator.Rss201rev2Feed
    title ="MyPodcastFeed"
    link = "/artikel/podcast"
    description = "A small podcast feed"

    def items(self):
        return Podcast.objects.order_by('-pod_pub_date')

    def item_description(self, item):
        return item.get_podcast_desc()

    def item_link(self, item):
        return item.get_absolute_url()

    def item_enclosure_url(self, item):
        return item.get_enclosure_url()

    def item_enclosure_length(self, item):
        return item.get_enclosure_length()
 
    def item_enclosure_mime_type(self, item):
        return item.get_enclosure_mime_type()


