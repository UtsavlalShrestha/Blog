from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class BlogAdd(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']
