from django.shortcuts import render

# Create your views here.
def events(request):
    return render(request, 'events/events.html')

def eventsFilter(request):
    return render(request, 'events/eventsFilter.html')
