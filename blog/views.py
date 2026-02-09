from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def single_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  
    return render(request, 'website/post.html', {'post': post}) 
