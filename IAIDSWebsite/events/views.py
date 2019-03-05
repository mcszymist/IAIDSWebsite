from django.shortcuts import render
from orgAdminPanel.models import Event
# Create your views here.
def events(request):
    allEvents = Event.objects.all()
    return render(request, 'events/events.html', {'allEvents': allEvents})

def eventsFilter(request):
    allEvents = Event.objects.all()
    return render(request, 'events/eventsFilter.html', {'allEvents': allEvents})
