from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html")),
]