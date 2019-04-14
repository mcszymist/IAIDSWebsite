from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect
from .models import Event, Organization, OrganizationUsers, MyUser, Job
from django.views.generic import FormView
from .forms import EventForm, UserForm
from django.http import JsonResponse
from datetime import datetime

@never_cache
def start(request):
    org_id = request.GET.get('org')
    obj = Organization.objects.get(id=org_id)
    request.session["org_id"] = org_id
    allEvents = Event.objects.all().filter(orgID=obj)
    allUsers = OrganizationUsers.objects.all().filter(orgID=obj)
    eventForm = EventForm()
    eventEditForm = EventForm(auto_id="edit_%s")
    userForm = UserForm(auto_id="user_%s")

    return render(request, 'orgAdminPanel/orgAdminPanel.html', {'eventEditForm': eventEditForm,'form': eventForm,'userForm': userForm,'allEvents': allEvents,'allUsers': allUsers})
    
def eventFoamPost(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            obj = Organization.objects.get(id=request.session["org_id"])
            info = form.cleaned_data
            org = Event(orgID = obj, name = info['name'],description=info['description'],location = info['location'],startdate = info['startdate'],enddate = info['enddate'],starttime = info['starttime'],endtime = info['endtime'])
            org.save()
            data = {
                'id':org.id,
                'message': "Successfully submitted form data.",
            }
            return JsonResponse(data)
        else:
            return JsonResponse(form.errors, status=400)
    return JsonResponse(status=404)
    
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
    return JsonResponse(status=404)
    
def eventEditFormPost(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            info = form.cleaned_data
            event = Event.objects.get(id=request.POST['edit_id'])
            event.name = info['name']
            event.description=info['description']
            event.location = info['location']
            event.startdate = info['startdate']
            event.enddate = info['enddate']
            event.starttime = info['starttime']
            event.endtime = info['endtime']
            event.save()
            data = {
                'id':event.id,
                'tableRow':request.POST['edit_tableRow'],
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return JsonResponse(form.errors, status=400)
    # if a GET (or any other method) we'll create a blank form
    return JsonResponse(status=404)
    
def DeleteEvent(request):
    id = request.POST.get('id', '')
    instance = Event.objects.get(id=id)
    instance.delete()
    data = {
                'id':id,
                'message': "Deleted Successfully.",
            }
    return JsonResponse(data,status=200)

def DeleteUser(request):
    id = request.POST.get('id', '')
    instance = OrganizationUsers.objects.get(orgID=id)
    instance.delete()
    data = {
                'id':id,
                'message': "Deleted Successfully.",
            }
    return JsonResponse(data,status=200)
    
def Back(request):
    return redirect("/yourOrganizations/")

def DeleteOrganization(request):
    id = request.GET.get('id', '')
    instance = Organization.objects.get(id=id)
    instance.delete()
    return redirect("/yourOrganizations/")
    
def getEvent(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        event = Event.objects.get(id=request.POST["id"])
        data = {
            'org': event.orgID.name,
            'name': event.name,
            'description': event.description,
            'location': event.location,
            'startdate': event.startdate,
            'enddate': event.enddate,
            'starttime': event.starttime,
            'endtime': event.endtime,
            'id': event.id,
            'message': "Successfully submitted form data.",
        }
        return JsonResponse(data)
    return JsonResponse(status=404)

# def getReport(obj):
#     #set the date and time format
#     date_format = "%H:%M:%S"
#     data = {}
#     all_event = Event.objects.all().filter(orgID=obj)
#     for event in all_event:
#         all_jobs = Job.objects.all().filter(eventID=event)
#         for job in all_jobs:
#             time1 = job.starttime
#             time2 = job.endtime
#             #calculate hours
#             date_format = "%H:%M:%S"
#             dtTime1 = datetime.strptime(str(time1), date_format)
#             dtTime2 = datetime.strptime(str(time2), date_format)
#             #diff = (dtTime2 - dtTime1).seconds

#             for user in job.userID.all():
#                 values = []
#                 values.append(str(user.first_name) + " " + str(user.last_name))
#                 values.append(str(user))
#                 #values.append(diff)
#                 data[str(user)] = 3
#     return data

                
                

        
            

        
            

        
        

         

