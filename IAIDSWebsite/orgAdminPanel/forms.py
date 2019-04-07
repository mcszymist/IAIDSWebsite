from django import forms
from .models import Event, OrganizationUsers
from django.forms import ModelForm
from django.forms import SelectDateWidget

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'location', 'startdate','enddate','starttime','endtime', 'description')
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Event Title'}),
			'location' : forms.TextInput(attrs={'placeholder': 'Location'}),
            'startdate' : forms.DateInput(attrs={'class': 'datepicker'}),
			'enddate' : forms.DateInput(attrs={'class': 'datepicker'}),
            'starttime' : forms.TimeInput(),
			'endtime' : forms.TimeInput(),
			'description' : forms.Textarea(),
            'type' : forms.Textarea(),
        }

class UserForm(forms.ModelForm):

    class Meta:
        model = OrganizationUsers
        fields = ('userID', 'privledge')
        widgets = {
            'userID' : forms.TextInput(attrs={'placeholder': 'Users Email'}),
            'privledge' : forms.NumberInput(),
        }

