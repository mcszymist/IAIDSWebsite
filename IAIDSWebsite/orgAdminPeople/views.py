from django.shortcuts import render

# Create your views here.
def orgAdminPeople(request):
    return render(request, 'orgAdminPeople/orgAdminPeople.html')
