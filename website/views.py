from django.shortcuts import render, redirect
from blog.models import Post
from website.models import Contact
from django.utils import timezone
from django.contrib import messages

def home_view(request):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    return render(request, 'website/index.html', {'posts':posts})

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('website:contact')
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'website/contact.html')