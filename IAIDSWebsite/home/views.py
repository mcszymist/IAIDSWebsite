from django.shortcuts import render

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/currentgame/')
    else:
        return render(request, 'home_template.html')