from django.shortcuts import render

# Create your views here.
def eventEdit(request):
    return render(request, 'eventEdit/eventEdit.html')
