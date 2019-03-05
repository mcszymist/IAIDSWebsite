from django import forms
from .models import Event, OrganizationUsers
from django.forms import ModelForm
from django.forms import SelectDateWidget

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'location', 'personelMax', 'startdate','enddate', 'description')
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Event Title'}),
			'location' : forms.TextInput(attrs={'placeholder': 'Location'}),
			'personelMax' : forms.NumberInput(),
            'startdate' : forms.DateTimeInput(),
			'enddate' : forms.DateTimeInput(),
			'description' : forms.Textarea(),
        }

class UserForm(forms.ModelForm):

    class Meta:
        model = OrganizationUsers
        fields = ('userID', 'privledge')
        widgets = {
            'userID' : forms.TextInput(attrs={'placeholder': 'Event Title'}),
            'privledge' : forms.NumberInput(),
        }

