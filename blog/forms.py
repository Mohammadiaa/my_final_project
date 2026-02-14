from django import forms
from .models import Comment
from website.models import Contact
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'required': True}),
        }

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()  

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'required': True}),
            }