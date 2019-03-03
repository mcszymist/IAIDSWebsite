from django.shortcuts import render
from orgAdminPanel.models import Organization
from django.views.generic import FormView
from .forms import OrganizationForm
from django.http import JsonResponse

# Create your views here.

class OrganizationFormView(FormView):
    form_class = OrganizationForm
    template_name  = 'yourOrganizations/yourOrganizations.html'
    success_url = '/yourOrganizations/'
    
    def get_context_data(self, **kwargs):
        context = super(OrganizationFormView, self).get_context_data(**kwargs)
        context['allOrgs'] = Organization.objects.all()
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
            
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response
     
