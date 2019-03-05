from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]



