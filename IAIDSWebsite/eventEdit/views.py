from django.shortcuts import render, redirect
from django.http import HttpResponse
from orgAdminPanel.models import Job, Event
import json

# Create your views here.
def eventEdit(request):
    id = request.GET.get('event', '')
    if id == '':
        return redirect('/yourOrganizations/') 
    else:
        eventInt = Event.objects.get(id=id)  # Getting all the events from database
        jobs = Job.objects.all().filter(eventID=eventInt)
        return render(request, 'eventEdit/eventEdit.html', { 'event': eventInt, 'allJobs':jobs })
    
def signupJob(request):
    id = request.POST.get('id', '')
    instance = Job.objects.get(id=id)
    instance.userID = self.request.user
    instance.save()
    return HttpResponse(json.dumps({'id': id}), content_type="application/json")
    
def updateDes(request):
    id = request.POST.get('id', '')
    des = request.POST.get('des', '')
    instance = Event.objects.get(id=id)
    instance.description = des
    instance.save()
    return HttpResponse(json.dumps({'id': id}), content_type="application/json")
    
def eventAdd(request):
    return render(request, 'eventEdit/eventEdit.html', { 'jobs': jobs })