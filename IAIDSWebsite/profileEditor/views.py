from django.shortcuts import render

# Create your views here.
def profileManage(request):
    return render(request, 'profileEditor/profileManage.html')