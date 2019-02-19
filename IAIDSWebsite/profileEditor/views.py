from django.shortcuts import render
from django.utils.encoding import smart_str
from django.http import HttpResponse
from IAIDSWebsite import settings

# Create your views here.
def profileManage(request):
    return render(request, 'profileEditor/profileManage.html')

def profileImage(request,file_name):
    image = settings.MEDIA_ROOT+'/profileEditor/'+file_name
    with open(image, "rb") as f:
        response = HttpResponse(f.read(), content_type="image/jpeg")
    response['X-Sendfile'] = smart_str(settings.MEDIA_ROOT+'/profileEditor/'+file_name)
    return response
