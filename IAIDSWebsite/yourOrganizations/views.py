from django.shortcuts import render
from orgAdminPanel.models import Organization, OrganizationUsers, Event
from django.views.generic import FormView
from .forms import OrganizationForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json
# Create your views here.

def DeleteOrg(request):
    org_id = request.POST.get('id', '')
    instance = get_object_or_404(Organization, id=org_id)
    instance.delete()
    return HttpResponse(json.dumps({'id': org_id}), content_type="application/json")
    
    
def my_view(request): 
    org_name = request.POST.get('id', '')
    instance = get_object_or_404(Organization, id=org_name)
    form = OrganizationForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        data = {
                'message': "Successfully submitted form data."
            }
        return JsonResponse(data)
    return JsonResponse(form.errors, status=400) 
     
class OrganizationFormView(FormView):
    form_class = OrganizationForm
    template_name  = 'yourOrganizations/yourOrganizations.html'
    success_url = '/yourOrganizations/'
    
    
    def get_context_data(self, **kwargs):      
        context = super(OrganizationFormView, self).get_context_data(**kwargs)
        users = OrganizationUsers.objects.all().filter(userID=self.request.user)
        objLen = []
        obj = []
        for user in users:
            obj.append((user.orgID,Event.objects.all().filter(orgID=user.orgID).count()))
        context['allOrgs'] = obj
        return context
        
    def form_invalid(self, form):
        response = super(OrganizationFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(OrganizationFormView, self).form_valid(form)
        if self.request.is_ajax():
            info = form.cleaned_data
            #print(info)
            org = Organization(name = info['name'],description=info['description'])
            org.save()
            newOrgUser = OrganizationUsers(userID = self.request.user, orgID = org, privledge = 3)
            newOrgUser.save()
            data = {
                'message': "Successfully submitted form data.",
                'id': org.id
            }
            return JsonResponse(data)
        else:
            return response
     
