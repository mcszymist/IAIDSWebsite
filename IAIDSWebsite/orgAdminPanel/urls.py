from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('eventSave/', views.eventFoamPost, name='eventFoamPost'),
    path('userSave/', views.userFoamPost, name='UserFormView'),
    path('eventEdit/', views.eventEditFormPost, name='eventEditFormPost'),
    path('delete/', views.DeleteEvent, name='DeleteEvent'),
    path('deleteOrg/', views.DeleteOrganization, name='DeleteOrganization'),
    path('deleteUser/', views.DeleteUser, name='DeleteUser'),
    path('getEvent/',views.getEvent, name='getEvent'),
    path('eventCSV/<eventId>',views.event_csv, name='event_csv'), 
]
