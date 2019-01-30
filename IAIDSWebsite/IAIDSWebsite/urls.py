from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('home.urls')),
    path('createAccount/', include('createAccount.urls')),
    path('profileedit/', include('profileEditor.urls')),
    path('admin/', admin.site.urls),
]
