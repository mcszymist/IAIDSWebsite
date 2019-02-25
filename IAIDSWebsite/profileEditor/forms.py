from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
from createAccount.models import MyUser

#moduleName = input('Enter module name:')
#importlib.import_module(moduleName)

class profileEditForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['email',
                  'first_name',
                  'last_name',
                  'description',
                  'password',
                  'profile_pic'
                  ]