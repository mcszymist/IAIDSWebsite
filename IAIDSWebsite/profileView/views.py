from django.shortcuts import render

# Create your views here.
def profileView(request):
    return render(request, 'profileView/profileView.html')
