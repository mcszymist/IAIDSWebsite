from django.shortcuts import render, get_object_or_404
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.http import JsonResponse
from IAIDSWebsite import settings
from createAccount import models
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import profileEditForm
from django.contrib.auth.models import User

# Create your views here.


def toggle_is_org_owner(request):
    if request.user.is_org_owner == True:
        request.user.is_org_owner = False
    else:
        request.user.is_org_owner = True
    request.user.save()
    data = {
        'owner':request.user.is_org_owner,
        'message': "Successfully submitted form data.",
    }
    return JsonResponse(data)


def profileManage(request):
    user_id = request.GET.get('user', '')
    if user_id == '':
        instance = request.user
    else:
        instance = get_object_or_404(models.MyUser, id=user_id)
    messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'profileEditor/profileManage.html', {'profile': instance})


def profileEvents(request):
    user_id = request.GET.get('user', '')
    if user_id == '':
        instance = request.user
    else:
        instance = get_object_or_404(models.MyUser, id=user_id)
    return render(request, 'profileEditor/profileEvents.html', {'profile': instance})


def profileImage(request, file_name):
    image = settings.MEDIA_ROOT+'/profileEditor/'+file_name
    with open(image, "rb") as f:
        response = HttpResponse(f.read(), content_type="image/jpeg")
    response['X-Sendfile'] = smart_str(settings.MEDIA_ROOT +
                                       '/profileEditor/'+file_name)
    return response


def edit(request):
    curr_email = request.user.email
    curr_user = models.MyUser.objects.get(email=curr_email)
    form = profileEditForm(request.POST, request.FILES,
                           instance=curr_user)
    if request.method == 'POST':
        form = profileEditForm(request.POST, request.FILES,
                               instance=curr_user)
        if form.is_valid():
            curr_user = form.save()
            return redirect('profileManage')

    else:
        form = profileEditForm(instance=request.user)

    return render(request, 'profileEditor/profileEdit.html', {'form': form})
