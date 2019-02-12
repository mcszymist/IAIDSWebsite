from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms



class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    email = forms.CharField(widget=TextInput(attrs={'placeholder':'Email'}))
    class Meta:
        model = User
        fields = {
            'username',
            'email',
            'password'   
        }
   
    
