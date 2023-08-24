from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', max_length=50)
    email = forms.EmailField(label='Email', required=True)
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

