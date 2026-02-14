from django.db import models
from captcha.fields import CaptchaField
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    active = models.BooleanField(default=True)
    superuser = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['-created_date']