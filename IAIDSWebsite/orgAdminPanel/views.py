
from django.shortcuts import render, redirect
from .models import Event, Organization, OrganizationUsers, MyUser
from django.views.generic import FormView
from .forms import EventForm, UserForm
from django.http import JsonResponse

def eventFoamPost(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            obj = Organization.objects.get(id=request.session["org_id"])
            info = form.cleaned_data
            #print(info)
            org = Event(orgID = obj, name = info['name'],description=info['description'],location = info['location'],startdate = info['startdate'],enddate = info['enddate'],starttime = info['starttime'],endtime = info['endtime'])
            org.save()
            data = {
                'id':org.id,
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    else:
        org_id = request.GET.get('org')
        obj = Organization.objects.get(id=org_id)
        request.session["org_id"] = org_id
        allEvents = Event.objects.all().filter(orgID=obj)
        allUsers = OrganizationUsers.objects.all().filter(orgID=obj)
        eventForm = EventForm()
        userForm = UserForm()

    return render(request, 'orgAdminPanel/orgAdminPanel.html', {'form': eventForm,'userForm': userForm,'allEvents': allEvents,'allUsers': allUsers})
    
def userFoamPost(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            info = form.cleaned_data
            obj = Organization.objects.get(id=request.session["org_id"])
            user = MyUser.objects.get(email=info['userID'])
            #print(info)
            org = OrganizationUsers(orgID = obj,userID = user,privledge = info['privledge'])
            org.save()
            data = {
                'id':org.id,
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return JsonResponse(form.errors, status=400)
    # if a GET (or any other method) we'll create a blank form
    else:
        org_id = request.GET.get('org')
        request.session["org_id"] = org_id
        obj = Organization.objects.get(id=org_id)
        allEvents = Event.objects.all().filter(orgID=obj)
        allUsers = OrganizationUsers.objects.all().filter(orgID=obj)
        eventForm = EventForm()
        userForm = UserForm()

    return render(request, 'orgAdminPanel/orgAdminPanel.html', {'form': eventForm,'userForm': userForm,'allEvents': allEvents,'allUsers': allUsers})

def DeleteEvent(request):
    id = request.POST.get('id', '')
    instance = Event.objects.get(id=id)
    instance.delete()
    
def Back(request):
    return redirect("/yourOrganizations/")

def DeleteOrganization(request):
    id = request.GET.get('id', '')
    instance = Organization.objects.get(id=id)
    instance.delete()
    return redirect("/yourOrganizations/")
    