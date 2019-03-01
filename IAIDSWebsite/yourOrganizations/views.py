from django.shortcuts import render
from orgAdminPanel.models import Organization
# Create your views here.
def yourOrganizations(request):
    allOrgs = Organization.objects.all()
    return render(request, 'yourOrganizations/yourOrganizations.html', {'orgs':	allOrgs})
