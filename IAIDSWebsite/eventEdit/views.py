from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from orgAdminPanel.models import Job, Event
from .forms import JobForm
import json
from django.views.generic import FormView
# Create your views here.
    
def signUpJob(request):
    id = request.POST.get('id', '')
    instance = Job.objects.get(id=id)
    instance.userID = self.request.user
    instance.save()
    return HttpResponse(json.dumps({'id': id}), content_type="application/json")
    
def updateDes(request):
    id = request.POST.get('id', '')
    des = request.POST.get('des', '')
    instance = Event.objects.get(id=id)
    instance.page = des
    instance.save()
    return HttpResponse(json.dumps({'id': id}), content_type="application/json")
    
class JobFormView(FormView):
    form_class = JobForm
    template_name  = 'eventEdit/eventEdit.html'
    success_url = '/eventEdit/join/'
    
    def get_context_data(self, **kwargs):
        context = super(JobFormView, self).get_context_data(**kwargs)
        id = self.request.GET.get('event', '')
        if id == '':
            return redirect('/') 
        else:
            self.request.session["event_id"] = id
            context['event'] = Event.objects.get(id=id)  # Getting all the events from database
            context['allJobs'] = Job.objects.all().filter(eventID=self.request.session["event_id"])
            return context
        
    def form_invalid(self, form):
        response = super(JobFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(JobFormView, self).form_valid(form)
        if self.request.is_ajax():
            obj = Event.objects.get(id=self.request.session["event_id"])
            info = form.cleaned_data
            #print(info)
            job = Job(eventID = obj, name = info['name'],description=info['description'],personelMax = info['personelMax'],startdate = info['startdate'],enddate = info['enddate'])
            job.save()
            
            data = {
                'id': job.id,
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response
