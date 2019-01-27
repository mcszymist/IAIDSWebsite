from django.shortcuts import render

# Create your views here.

def createAccount(request):
    return render(request, 'createAccount/createAccount.html')