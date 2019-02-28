
from .forms import EventForm
from django.shortcuts import render, redirect

# Create your views here.
def orgAdminPanel(request):
    return render(request, 'orgAdminPanel/orgAdminPanel.html')

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('./')  

    else:
        form = EventForm()
    
    return render(request, 'orgAdminPanel/orgAdminPanel.html', {'form': form})

