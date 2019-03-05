from django import forms
from orgAdminPanel.models import Organization
from django.forms import ModelForm
from django.forms import SelectDateWidget
    
class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ('name', 'description')
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Organization Name'}),
			'description' : forms.Textarea(),
        }