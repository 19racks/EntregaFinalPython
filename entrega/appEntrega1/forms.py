from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import BlogPost, ContactMessage, TeamMember

from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'content', 'category', 'imagen']

class ContactMessageForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    message = forms.CharField(max_length=700)

class TeamMemberForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.EmailField()
    githubaccount = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k: "" for k in fields}

class UserUpdateForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        help_texts = {k: "" for k in fields}

