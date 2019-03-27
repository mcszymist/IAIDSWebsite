from django import forms
from orgAdminPanel.models import Job
from django.forms import ModelForm
from django.forms import SelectDateWidget

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('name', 'personelMax', 'startdate','enddate', 'starttime','endtime','description')
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Job Title'}),
			'personelMax' : forms.NumberInput(),
            'startdate' : forms.DateInput(attrs={'class': 'datepicker'}),
			'enddate' : forms.DateInput(attrs={'class': 'datepicker'}),
            'starttime' : forms.TimeInput(),
			'endtime' : forms.TimeInput(),
			'description' : forms.Textarea(),
        }