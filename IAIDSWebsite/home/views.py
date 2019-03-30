from django.shortcuts import render
from django.http import HttpResponseRedirect
from allauth.account.views import LoginView
from allauth.account.forms import LoginForm
from .forms import MyCustomLoginForm

# Create your views here.


class MyCustomLoginView(LoginView):
   
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context=super(MyCustomLoginView, self).get_context_data(*args, **kwargs)
        context['login_form'] = LoginForm()
        return context


  
