from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post

class LatestPostsFeed(Feed):
    title = "Latest Blog Posts"
    link = "/blog/"
    description = "Newest posts from the blog"

    def items(self):
        return Post.objects.filter(status=1).order_by('-published_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:200]

    def item_link(self, item):
        return reverse('blog:single', args=[item.id])
