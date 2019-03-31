from django.shortcuts import render
from django.http import HttpResponseRedirect
from allauth.account.views import LoginView
from allauth.account.forms import LoginForm
from .forms import MyCustomLoginForm

# Create your views here.


def index(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('')
    # else:
    return render(request, 'home.html')


  
