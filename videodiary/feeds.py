from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.utils.feedgenerator import Rss201rev2Feed
from django.conf import settings

from videodiary.models import Post, Category

class Podcast(Rss201rev2Feed):
    def root_attributes(self):
        attrs = super(Podcast, self).root_attributes()
        attrs['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
        return attrs

    def add_root_elements(self, handler):
        super(Podcast, self).add_root_elements(handler)
        handler.addQuickElement('itunes:explicit', 'explicit')
        handler.addQuickElement('itunes:author', 'Jonny Flynn')
        handler.addQuickElement('itunes:category', 'Basketball')

class LatestPosts(Feed):
    feed_type = Podcast
    title = "Johnny Flynn's Draft Diary Latest Posts"
    link = "/"
    copyright = "&#x2117; &amp; &#xA9; 2009 Jonny Flynn &amp; Levi's"
    description = "Updates on changes and additions to Jonny Flynn's Levi's Draft Diary"
    item_enclosure_mime_type = "video/quicktime"

    def items(self):
        return Post.objects.filter(is_public=True).order_by('-date_added')[:5]

    def item_pubdate(self, item):
        return item.date_added
    
    def item_enclosure_url(self, item):
        return 'http://%s%s' % (Site.objects.get_current().domain, item.podcast_video.url)

    def item_enclosure_length(self, item):
        return item.podcast_video.size
    
class LatestPostsByCategory(Feed):
    feed_type = Podcast
    copyright = "&#x2117; &amp; &#xA9; 2009 Jonny Flynn &amp; Levi's"
    description = "Updates on changes and additions to Levi's Draft Diary"
    item_enclosure_mime_type = "video/quicktime"

    def get_object(self, bits):
        if len(bits) != 1:
            raise ObjectDoesNotExist
        return Category.objects.get(title_slug__exact=bits[0])

    def title(self, obj):
        return "Johnny Flynn %s Latest Posts" % obj.title
    
    def link(self, obj):
        if not obj:
            raise FeedDoesNotExist
        return obj.get_absolute_url()

    def items(self, obj):
        category = Category.objects.filter(id__exact=obj.id).get()
        items = category.latest()
        return items
    
    def item_enclosure_url(self, item):
        return 'http://%s%s' % (Site.objects.get_current().domain, item.podcast_video.url)

    def item_enclosure_length(self, item):
        return item.podcast_video.size