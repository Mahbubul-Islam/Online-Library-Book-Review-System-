from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Review

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required= True,
        widget= forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'})
    )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        Widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}), 
        }