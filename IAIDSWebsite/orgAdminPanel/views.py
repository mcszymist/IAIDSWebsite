from django.shortcuts import render

# Create your views here.
def orgAdminPanel(request):
    return render(request, 'orgAdminPanel/orgAdminPanel.html')
