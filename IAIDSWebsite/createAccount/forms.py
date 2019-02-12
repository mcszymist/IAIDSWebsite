from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms

class CustomAuthForm(AuthenticationForm):
    first_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    def __init__(self, *args, **kwargs):
        super(CustomAuthForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", 'password2')


