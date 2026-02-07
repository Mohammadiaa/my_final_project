from django.shortcuts import render

# Create your views here.
def posts_view(request):
    return render(request, 'core/index.html' )

def single_view(request):
    return render(request, 'core/post.html' )