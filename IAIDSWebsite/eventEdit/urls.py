from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.JobFormView.as_view(), name='JobFormView'),
    path('signUpJob/', views.signUpJob,name='signUpJob'),
    path('signOutJob/', views.signOutJob,name='signOutJob'),
    path('deleteJob/', views.deleteJob,name='deleteJob'),
    path('updateDes/', views.updateDes,name='updateDes')
]
