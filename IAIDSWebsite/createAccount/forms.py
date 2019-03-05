
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class SignUpForm(UserCreationForm):
    class Meta:
        password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
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
        
    
