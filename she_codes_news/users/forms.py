from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # to register/sign up as a new user
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'business_name', 'type', 'bio', 'linkedin_url', 'profile_photo']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class':'form-input', 'placeholder':'Enter email address', 'type':'email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'business_name': forms.TextInput(attrs={'class': 'form-input'}),
            'type': forms.Select(attrs={'class': 'form-imput', 'default': 'Founder'}),
            'bio': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Tell us about you and your business'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Paste your LinkedIn URL here'}),
        }

class CustomUserChangeForm(UserChangeForm):
    # to make changes to an existing user
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'business_name', 'type', 'bio', 'linkedin_url', 'profile_photo']