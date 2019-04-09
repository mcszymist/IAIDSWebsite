from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.start, name='yourOrganizations'),
    path('orgSave/', views.OrganizationFormView, name='OrganizationFormView'),
    path('orgEdit/', views.OrganizationEditFormView, name='OrganizationEditFormView'),
    path('delete/', views.DeleteOrg, name='deleteOrg'),
]
