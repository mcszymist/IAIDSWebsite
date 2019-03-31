from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='createAccount/password_reset.html'
         ),
         name='password_reset'),
    path('activate/<uidb64>/<token>/',
        views.activate, name='activate'),
]



