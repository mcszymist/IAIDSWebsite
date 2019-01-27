from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('home.urls')),
    path('profileeditor/', include('profileEditor.urls')),
]
