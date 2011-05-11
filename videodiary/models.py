from datetime import datetime
import random
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from videologue.models import Video, Gallery

class Category(Gallery):
    is_header = models.BooleanField(_('is header'), default=False, 
        help_text=_('Set this to true for the category to appear as a link in the top navigation.'))

    class Meta:
        ordering = ['date_added']
        get_latest_by = 'date_added'
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):
        return reverse('category', args=[self.title_slug])

    def latest(self, limit=0, public=True):
        if limit == 0:
            limit = self.video_count()
        if public:
            return self.public()[:limit]
        else:
            return self.videos.filter(flv_video__isnull=False)[:limit]

    def sample(self, count=0, public=True):
        if count == 0 or count > self.video_count():
            count = self.video_count()
        if public:
            video_set = self.public()
        else:
            video_set = self.videos.filter(flv_video__isnull=False)
        return random.sample(video_set, count)

    def video_count(self, public=True):
        if public:
            return self.public().count()
        else:
            return self.videos.filter(flv_video__isnull=False).count()
    video_count.short_description = _('count')

    def public(self):
        return self.videos.filter(flv_video__isnull=False, is_public=True)

class Post(Video):
    allow_comments  = models.BooleanField(_('allow comments'), default=True)
    oembed          = models.CharField(_('oembed URL (video)'), help_text=_('Enter the URL for a video at an online video service like Vimeo.'), max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['-date_added']
        get_latest_by = 'date_added'
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('video_post', (), {
            'year': self.date_added.year,
            'month': "%02d" % self.date_added.month,
            'slug_field': self.title_slug
    })

    def __str__(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        if self.title_slug is None:
            self.title_slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
class Ad(Video):
    class Meta:
        ordering = ['-date_added']
        get_latest_by = 'date_added'
        verbose_name = _("ad")
        verbose_name_plural = _("ads")

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        if self.title_slug is None:
            self.title_slug = slugify(self.title)
        super(Ad, self).save(*args, **kwargs)
        
from django.contrib.comments.signals import comment_was_posted

def on_comment_was_posted(sender, comment, request, *args, **kwargs):
        # spam checking can be enabled/disabled per the comment's target Model
        #if comment.content_type.model_class() != Entry:
        #    return

        from django.contrib.sites.models import Site
        from django.conf import settings

        try:
                from akismet import Akismet
        except:
                return

        # use TypePad's AntiSpam if the key is specified in settings.py
        if hasattr(settings, 'TYPEPAD_ANTISPAM_API_KEY'):
                ak = Akismet(
                        key=settings.TYPEPAD_ANTISPAM_API_KEY,
                        blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
                )
                ak.baseurl = 'api.antispam.typepad.com/1.1/'
        else:
                ak = Akismet(
                key=settings.AKISMET_API_KEY,
                blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
        )

        if ak.verify_key():
                data = {
                        'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
                        'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                        'referrer': request.META.get('HTTP_REFERER', ''),
                        'comment_type': 'comment',
                        'comment_author': comment.user_name.encode('utf-8'),
                }

                if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
                        if hasattr(comment.content_object,'author'):
                                user = comment.content_object.author
                        else:
                                from django.contrib.auth.models import User
                                user = User.objects.filter(is_superuser=True)[0]

                        comment.flags.create(
                                user=user,
                                flag='spam'
                        )
                        comment.is_public = False
                        comment.save()

comment_was_posted.connect(on_comment_was_posted)