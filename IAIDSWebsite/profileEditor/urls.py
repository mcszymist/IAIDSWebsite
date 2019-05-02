from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.profileManage, name='profileManage'),
    path('edit', views.edit, name='edit'),
    path('events', views.profileEvents, name='profileEvents'),
    path('ownerToggle',views.toggle_is_org_owner, name='toggle_is_org_owner'),
]
