from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from profileEditor.views import profileImage


urlpatterns = [
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('eventEdit/', include('eventEdit.urls')),
    path('events/', include('events.urls')),
    path('orgAdminPanel/', include('orgAdminPanel.urls')),
    path('profileView/', include('profileView.urls')),
    path('yourOrganizations/', include('yourOrganizations.urls')),
    path('createAccount/', include('createAccount.urls')),
    path('images/profileEditor/<file_name>',
         profileImage, name='profile_image'),
    path('profile/', include('profileEditor.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
