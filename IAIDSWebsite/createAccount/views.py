# from django.shortcuts import render

# # Create your views here.

# def createAccount(request):
#     return render(request, 'createAccount/createAccount.html')

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm



def signup(request):
    title = "Register"
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        user = authenticate(username = user.username, password=password)
        login(request, user)
        return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'createAccount/signup.html', {'form': form})