from django.shortcuts import render
from django import forms
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from .admin import UserCreationForm
from .forms import SignUpForm
from .models import MyUser





def signup(request):
    title = "Register"
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.set_unusable_password()
            user.save()
            current_site = get_current_site(request)
            # Send an email to the user with the token:
            mail_subject = 'Activate your account.'
            message = render_to_string('createAccount/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).encode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            #return redirect('/')
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = UserCreationForm()
    return render(request, 'createAccount/signup.html', {'form': form})

#From a tutorial will post link if it works.
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        #return redirect('./')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
