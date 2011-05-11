from django.conf import settings
from django.conf.urls.defaults import *
from videodiary.feeds import LatestPosts, LatestPostsByCategory

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

feeds = {
    'latest': LatestPosts,
    'categories': LatestPostsByCategory,
}

urlpatterns = patterns('',
    # Example:
#     (r'^draftdiary/', include('draftdiary.foo.urls')),
    url(r'^$', 'videodiary.views.home', name='home'),
    url(r'^post/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug_field>[-\w]+)/$', 'videodiary.views.post', name='video_post'),
    url(r'^category/(?P<slug_field>[-\w]+)/$', 'videodiary.views.category', name='category'),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^', include('videodiary.urls')),
    (r'^comments/', include('threadedcomments.urls')),

    (r'^admin/filebrowser/', include('filebrowser.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
