from django.shortcuts import render
from django.http import HttpResponse
from orgAdminPanel.models import Event

# Create your views here.
def eventEdit(request):
    events = Event.objects.all()  # Getting all the events from database
    return render(request, 'eventEdit/eventEdit.html', { 'events': events })

def eventAdd(request):
    return render(request, 'eventEdit/eventEdit.html', { 'events': events })