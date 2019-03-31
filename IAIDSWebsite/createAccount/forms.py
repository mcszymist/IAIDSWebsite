
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password'}))
    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'password1' ,'password2')

        widgets = {
            
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email'}),
        }

        
        
    
