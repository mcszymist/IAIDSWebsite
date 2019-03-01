from django import forms
from .models import Event
from django.forms import ModelForm
from django.forms import SelectDateWidget

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'location', 'personelMax', 'startdate','enddate', 'description')
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Event Title'}),
			'location' : forms.TextInput(attrs={'placeholder': 'Event Title'}),
			'personalMax' : forms.NumberInput(),
            'startdate' : forms.DateTimeInput(),
			'enddate' : forms.DateTimeInput(),
			'description' : forms.Textarea(),
        }

