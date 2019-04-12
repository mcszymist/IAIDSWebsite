from django.views.decorators.cache import never_cache
from django.shortcuts import render
from orgAdminPanel.models import Organization, OrganizationUsers, Event
from django.views.generic import FormView
from .forms import OrganizationForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json
# Create your views here.

def DeleteOrg(request):
    org_id = request.POST.get('id', '')
    instance = get_object_or_404(Organization, id=org_id)
    instance.delete()
    return HttpResponse(json.dumps({'id': org_id}), content_type="application/json")
    
    
def my_view(request): 
    org_name = request.POST.get('id', '')
    instance = get_object_or_404(Organization, id=org_name)
    form = OrganizationForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        data = {
                'message': "Successfully submitted form data."
            }
        return JsonResponse(data)
    return JsonResponse(form.errors, status=400) 

@never_cache
def start(request):
    form = OrganizationForm()
    editForm = OrganizationForm(auto_id="edit_%s")
    users = OrganizationUsers.objects.all().filter(userID=request.user)
    obj = []
    for user in users:
        obj.append((user.orgID,Event.objects.all().filter(orgID=user.orgID).count()))
    allOrgs = obj
    return render(request, 'yourOrganizations/yourOrganizations.html', {'allOrgs': allOrgs,'form':form,'editForm':editForm})

def OrganizationFormView(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrganizationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            info = form.cleaned_data
            #print(info)
            org = Organization(name = info['name'],description=info['description'])
            org.save()
            newOrgUser = OrganizationUsers(userID = request.user, orgID = org, privledge = 3)
            newOrgUser.save()
            data = {
                'id': org.id,
                'message': "Successfully submitted form data.",
                
            }
            return JsonResponse(data)
        else:
            return JsonResponse(form.errors, status=400)
    return JsonResponse(status=404)

def OrganizationEditFormView(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrganizationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            info = form.cleaned_data
            org = Organization.objects.get(id=request.POST['edit_id'])
            org.name = info['name']
            org.description=info['description']
            org.save()
            data = {
                'id': org.id,
                'tableRow':request.POST['edit_tableRow'],
                'message': "Successfully edited organization.",
            }
            return JsonResponse(data)
        else:
            return JsonResponse(form.errors, status=400)
    return JsonResponse(status=404)
    
