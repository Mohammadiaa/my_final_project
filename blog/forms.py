from django import forms
from .models import Comment
from website.models import Contact
from captcha.fields import CaptchaField
from .models import CustomUser
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
        
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            from .models import CustomUser
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                raise forms.ValidationError("Invalid username or password!")

            if not user.check_password(password):
                raise forms.ValidationError("Invalid username or password!")

            cleaned_data['user'] = user

        return cleaned_data
