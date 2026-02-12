from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def single_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post 
            comment.save()
            messages.success(request, "Your comment was submitted successfully!")
            return redirect('blog:single', post_id=post.id)
        else:
            messages.error(request, "There was an error with your comment. Please check the form.")
    else:
        form = CommentForm()

    post.counted_view += 1
    post.save(update_fields=['counted_view'])

    return render(request, 'website/post.html', {
    'post': post,
    'form': form
})


def search_view(request):
    query = request.GET.get('q')
    results = Post.objects.none()

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(categories__name__icontains=query) |
            Q(tags__name__icontains=query),
            status=1
        ).distinct()
    
    context = {
        'query':query,
        'results': results
    }
    return render(request, 'website/search.html', context)


def category_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(categories=category, status=1)


    context = {
        'results': posts, 
        'query': category.name
    }
    return render(request, 'website/search.html', context)