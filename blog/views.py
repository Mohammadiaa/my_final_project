from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm
from django.utils import timezone
from django.contrib import messages
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
