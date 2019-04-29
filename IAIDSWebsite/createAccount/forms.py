
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from zxcvbn_password.fields import PasswordField, PasswordConfirmationField

class SignUpForm(UserCreationForm):
    password1 = PasswordField(label="Password")
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password'}))
    #password2 = PasswordConfirmationField(confirm_with='password1')

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

        
        
    
