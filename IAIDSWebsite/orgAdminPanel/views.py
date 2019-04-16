from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect
from .models import Event, Organization, OrganizationUsers, MyUser, Job
from django.views.generic import FormView
from .forms import EventForm, UserForm
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
import csv

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
    report = getReport(obj)

    return render(request, 'orgAdminPanel/orgAdminPanel.html', {'eventEditForm': eventEditForm,'form': eventForm,'userForm': userForm,'allEvents': allEvents,'allUsers': allUsers, 'report':report})
    
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

def getReport(obj):
    #set the date and time format
    date_format = "%H:%M:%S"
    data = {}
    all_event = Event.objects.all().filter(orgID=obj)
    for event in all_event:
        all_jobs = Job.objects.all().filter(eventID=event)
        for job in all_jobs:
            time1 = job.starttime.replace(microsecond = 0)
            time2 = job.endtime.replace(microsecond = 0)
            dtTime1 = datetime.strptime(str(time1) ,date_format)
            dtTime2 = datetime.strptime(str(time2) ,date_format)
            #calculate hours
            diff = dtTime2 - dtTime1
            hours = (diff.seconds/60)/60
           

            for user in job.userID.all():
                values = []
                values.append(str(user.first_name) + " " + str(user.last_name))
                values.append(str(user))
                values.append(hours)
                if(str(user) in data.keys()):      
                    newValue = data[str(user)]
                    newValue[2] += hours
                    data[str(user)] = newValue
                else:
                    data[str(user)] = values
    return data

def event_csv(request, eventId):
    eventId = eventId
    data = {} ## Will precent multiple users for showing up
    all_jobs = Job.objects.all().filter(eventID=eventId)
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="event.csv"'
    writer = csv.writer(response)
    writer.writerow(['FIRST_NAME', 'LAST_NAME', 'EMAIL', '', "DID SHOW?"])
    for job in all_jobs:
        for user in job.userID.all():
            if(str(user) not in data.keys()):
                writer.writerow([user.first_name, user.last_name, user])
                data[str(user)] = user
    return response

def report_csv(request, eventId):
     #duplicate code to download a csv
     #set the date and time format
    date_format = "%H:%M:%S"
    data = {}
    all_event = Event.objects.all().filter(orgID=obj)
    for event in all_event:
        all_jobs = Job.objects.all().filter(eventID=event)
        for job in all_jobs:
            time1 = job.starttime.replace(microsecond = 0)
            time2 = job.endtime.replace(microsecond = 0)
            dtTime1 = datetime.strptime(str(time1) ,date_format)
            dtTime2 = datetime.strptime(str(time2) ,date_format)
            #calculate hours
            diff = dtTime2 - dtTime1
            hours = (diff.seconds/60)/60
           

            for user in job.userID.all():
                values = []
                values.append(str(user.first_name) + " " + str(user.last_name))
                values.append(str(user))
                values.append(hours)
                if(str(user) in data.keys()):      
                    newValue = data[str(user)]
                    newValue[2] += hours
                    data[str(user)] = newValue
                else:
                    data[str(user)] = values

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    writer = csv.writer(response)
    writer.writerow(['NAME', 'EMAIL', '', "HOURS"])
    for users in data:
        writer.writerow([users[0], users[1], '', users[2]])
      
    return response



          
                

        
            

        
            

        
        

         

