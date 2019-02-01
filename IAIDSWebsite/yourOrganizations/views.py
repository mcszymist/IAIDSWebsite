from django.shortcuts import render

# Create your views here.
def yourOrganizations(request):
    return render(request, 'yourOrganizations/yourOrganizations.html')
