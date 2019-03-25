from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.eventEdit, name='eventEdit'),
    path('signUpJobs/', views.signupJob,name='signUpJobs'),
    path('updateDes/', views.updateDes,name='updateDes')
]
