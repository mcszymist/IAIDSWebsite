
from django.shortcuts import render, redirect
from .models import Event, Organization, OrganizationUsers
from django.views.generic import FormView
from .forms import EventForm, UserForm
from django.http import JsonResponse

# Create your views here.
def orgAdminPanel(request):
    allEvents = Event.objects.all()
    return render(request, 'orgAdminPanel/orgAdminPanel.html', {'allEvents': allEvents})

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
    
class EventFormView(FormView):
    form_class = EventForm
    template_name  = 'orgAdminPanel/orgAdminPanel.html'
    success_url = '/orgAdminPanel/join/'
    
    def get_context_data(self, **kwargs):
        context = super(EventFormView, self).get_context_data(**kwargs)
        org_id = self.request.GET.get('org')
        self.request.session["org_id"] = org_id
        obj = Organization.objects.get(id=org_id)
        context['allEvents'] = Event.objects.all().filter(orgID=obj)
        context['allUsers'] = OrganizationUsers.objects.all().filter(orgID=obj)
        return context
        
    def form_invalid(self, form):
        response = super(EventFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(EventFormView, self).form_valid(form)
        if self.request.is_ajax():
            obj = Organization.objects.get(id=self.request.session["org_id"])
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
            return response
