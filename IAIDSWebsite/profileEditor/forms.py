from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
from createAccount import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

#moduleName = input('Enter module name:')
#importlib.import_module(moduleName)

class profileEditForm(UserChangeForm):
    class Meta:
        model = models.MyUser
        fields = [
                  'first_name',
                  'last_name',
                  'description',
                  'profile_pic'
                  ]
