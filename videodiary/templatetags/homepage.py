from django.template import Library
from django.template import RequestContext
from videodiary.models import Category

register = Library()

@register.inclusion_tag("includes/navigation.html")
def nav():
    nav_list = Category.objects.filter(is_header=True, is_public=True)
    return {"nav_list": nav_list}

@register.inclusion_tag("includes/categories.html")
def cat():
    category_list = Category.objects.filter(is_header=False, is_public=True)
    return {"cat": category_list}

