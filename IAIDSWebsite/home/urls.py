from django.urls import path, include
from django.contrib import admin
from allauth.account.forms import LoginForm
from . import views


urlpatterns = [
    path('', views.index, name='home'),
]