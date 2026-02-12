from django import template
from blog.models import Post
from django.utils import timezone


register = template.Library()


@register.simple_tag
def latest_posts(count=3):
    return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:count]

@register.filter
def approved_comments(comments):
    return comments.filter(approved=True)