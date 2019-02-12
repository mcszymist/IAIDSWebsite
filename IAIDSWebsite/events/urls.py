from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.events, name='events'),
    path('search', views.eventsFilter, name='eventsFilter'),
]
