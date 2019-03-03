from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.OrganizationFormView.as_view(), name='yourOrganizations'),
]
