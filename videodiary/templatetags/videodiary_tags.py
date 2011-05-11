from django import template
from django.template import RequestContext
from videodiary.models import Category

register = template.Library()

@register.inclusion_tag('videodiary/add_this.html')
def add_this(url,title):
        from django.contrib.sites.models import Site
        site = Site.objects.get_current()

        from django.conf import settings
        username = settings.ADD_THIS_USERNAME
        return {'url': url, 'title': title, 'username': username, 'site': site }
