from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.EventFormView.as_view(), name='EventFormView'),
    path('delete/', views.DeleteEvent, name='deleteEvent')
]
