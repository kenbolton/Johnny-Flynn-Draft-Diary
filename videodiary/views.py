from datetime import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_list, object_detail
from django.http import Http404, HttpResponse

from videodiary.models import Ad, Post, Category

# Enable ads sitewide, if there are any.
try:
    ad = Ad.objects.filter(is_public=True).order_by('?')[:1].get()
except:
    ad = None
    
def home(request):
    try:
        post = Post.objects.filter(is_public=True, galleries__id=1)[:1].get()
    except:
        post = None
    try:
        latest = Post.objects.filter(is_public=True).exclude(pk=post.pk)
    except:
        latest = None
    return render_to_response('videodiary/homepage.html', {
        'object': post,
        'ad': ad,
        'latest': latest,
        'FLOWPLAYER': settings.FLOWPLAYER
    }, context_instance=RequestContext(request))
    
def post(request, year, month, slug_field):
    post = get_object_or_404(Post, title_slug__exact=slug_field, date_added__year=int(year), date_added__month=int(month))
#    ad = Ad.objects.filter(is_public=True).order_by('?')[:1].get()
    try:
        latest = Post.objects.filter(is_public=True).exclude(pk=post.pk)[0:4]
    except:
        latest = None
    if not post:
        raise Http404
    return render_to_response('videodiary/post_detail.html', {
        'object': post,
        'ad': ad,
        'latest': latest,
        'FLOWPLAYER': settings.FLOWPLAYER
    }, context_instance=RequestContext(request))
    
def category(request, slug_field):
    category = get_object_or_404(Category, title_slug__exact=slug_field)
    try:
        latest = Post.objects.filter(galleries__title_slug=slug_field, is_public=True)
    except:
        raise Http404   
    if not category:
        raise Http404
    return render_to_response('videodiary/category_detail.html', {
        'category': category,
        'latest': latest,
    }, context_instance=RequestContext(request))