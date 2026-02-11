from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

def home_view(request):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    return render(request, 'website/index.html', {'posts':posts})

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

