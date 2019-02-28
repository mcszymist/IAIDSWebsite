from django import forms
from .models import Event
from django.forms import ModelForm
from django.forms import SelectDateWidget

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'location', 'personel', 'date', 'time')
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Name'}),
            # 'date' : forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing")),
        }

