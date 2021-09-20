from django import template
from ..models import Blog
from django.db.models import Count


register = template.Library()

@register.inclusion_tag('Music/tag.html')
def Recent():
    return {'Recent':Blog.objects.all().order_by('-Time'),
    }

@register.inclusion_tag('Music/tag2.html')
def View():
    return {'View':Blog.objects.all().annotate(count=Count('hits')).order_by('-count')[:5]
    }

@register.inclusion_tag('Music/tag3.html')
def Category():
    return {'category':Blog.objects.all()
    }