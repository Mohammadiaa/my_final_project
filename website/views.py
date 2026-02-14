from django.shortcuts import render, redirect
from blog.models import Post
from website.models import Contact
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import ContactForm

def home_view(request):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now()).order_by("-published_date")

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except  PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'website/index.html', {'posts':posts})



def about_view(request):
    return render(request, 'website/about.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('website:contact')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    
    return render(request, 'website/contact.html', {'form': form})
       