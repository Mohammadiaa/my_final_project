from django.shortcuts import render

# Create your views here.


def single_view(request, post_id):
      
    return render(request, 'blog/post.html', {'post_id': post_id}) 
