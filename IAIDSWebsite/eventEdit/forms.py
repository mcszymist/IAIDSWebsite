from django import forms
from orgAdminPanel.models import Job, Event
from django.forms import ModelForm
from django.forms import SelectDateWidget

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('name', 'personelMax', 'startdate','enddate', 'description')
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Job Title'}),
			'personelMax' : forms.NumberInput(),
            'startdate' : forms.DateInput(),
			'enddate' : forms.DateInput(),
            'starttime' : forms.TimeInput(),
			'endtime' : forms.TimeInput(),
			'description' : forms.Textarea(),
        }