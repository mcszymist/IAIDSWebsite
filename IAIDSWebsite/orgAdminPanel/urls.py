from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.eventFoamPost, name='EventFormSave'),
    path('test/', views.userFoamPost, name='UserFormView'),
    path('delete/', views.DeleteEvent, name='DeleteEvent'),
    path('deleteOrg/', views.DeleteOrganization, name='DeleteOrganization')
]
