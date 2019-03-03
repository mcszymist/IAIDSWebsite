from django import forms
from orgAdminPanel.models import Organization
from django.forms import ModelForm
from django.forms import SelectDateWidget
    
class OrganizationForm(forms.Form): # or forms.ModelForm
    name = forms.CharField(max_length=120)
    description = forms.CharField()