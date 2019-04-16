from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q

from orgAdminPanel.models import Organization, OrganizationUsers, Event, Job

from allauth.account.views import LoginView
from allauth.account.forms import LoginForm

from .forms import MyCustomLoginForm

from datetime import datetime, date, timedelta

# Create your views here.


def index(request):
    your_event = []
    current_user = request.user
    startdateBegin = datetime.today()
    startdateEnd = startdateBegin + timedelta(days=7)
    starttimeBegin = datetime.time(datetime.now())
    testArray = [startdateBegin, startdateEnd]
    upcomingEvents = Event.objects.all().order_by(
        'startdate', 'starttime', 'name').filter(startdate__range=[startdateBegin, startdateEnd])

    event = suggested_event(upcomingEvents)
    
    # if False:
    #     users = OrganizationUsers.objects.all().filter(userID=request.user)
    #     obj = []
    #     for user in users:
    #         obj.append(
    #             (user.orgID, Event.objects.all().filter(orgID=user.orgID).count()))
    #     allOrgs = obj

    if(current_user.is_authenticated):
        your_event = get_event(current_user)

    return render(request, 'home.html',
                  {'testArray': testArray,
                   'upcomingEvents': upcomingEvents,
                   'your_event': your_event,
                   'event': event})

def get_event(user):
    data = []
    startdateBegin = datetime.today()
    startdateEnd = startdateBegin + timedelta(days=7)
    all_event = Event.objects.all()
    all_jobs = Job.objects.all().order_by('startdate', 'starttime').filter(userID = user, startdate__range=[startdateBegin, startdateEnd])
    if (all_jobs.count() > 0):
        first_job = all_jobs.first()
        event = first_job.eventID.name
        date = first_job.eventID.startdate
        time = (str(first_job.eventID.starttime) +" - " + str(first_job.eventID.endtime))
        description = first_job.eventID.description
        data.append(event)
        data.append(date)
        data.append(time)
        data.append(description)
    return data

def suggested_event(upcomingEvents):
    data = []
    if(upcomingEvents.count() > 0):
        first_event = upcomingEvents.first()
        event = first_event.name
        date = first_event.startdate
        time = (str(first_event.starttime) +" - " + str(first_event.endtime))
        description = first_event.description
        data.append(event)
        data.append(date)
        data.append(time)
        data.append(description)
    return data
        




    



