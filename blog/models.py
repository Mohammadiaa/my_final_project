from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  
from django import forms
from django.urls import reverse
import hashlib
# Create your models here.


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)  
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name   



class Post(models.Model):

    STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Published'),
    )

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    content = models.TextField()
    categories = models.ManyToManyField(Category, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    counted_view = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
    
    def get_absolute_url(self):
        return reverse('blog:single', args=[self.pk])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} on {self.post.title}"
    
class CustomUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)

    def set_password(self, raw_password):
        self.password = hashlib.sha256(raw_password.encode()).hexdigest()
    
    def check_password(self, raw_password):
        return self.password == hashlib.sha256(raw_password.encode()).hexdigest()
    
    def __str__(self):
        return self.username