from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.eventFoamPost, name='EventFormSave'),
    path('userSave/', views.userFoamPost, name='UserFormView'),
    path('eventEdit/', views.eventEditFormPost, name='eventEditFormPost'),
    path('delete/', views.DeleteEvent, name='DeleteEvent'),
    path('deleteOrg/', views.DeleteOrganization, name='DeleteOrganization')
]
