from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def single_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  

    post.counted_view += 1
    post.save(update_fields=['counted_view'])

    return render(request, 'website/post.html', {'post': post}) 
