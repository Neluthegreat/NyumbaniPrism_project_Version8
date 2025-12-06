"""
URL configuration for prism_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# CHANGE #1: Import the include function
from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    # CHANGE #2: Add a path that points to your panel app's URLs
    path('panel/', include('panel.urls')),
    path('accounts/', include('accounts.urls')),
    #path('', lambda request: redirect('login')), 
     path('HoD_Development/',include('HoD_Development.urls')), # Redirect root to login
      path('', RedirectView.as_view(url='/HoD_Development/dashboard/', permanent=True)),
      path('Developer_staff/', include('Developer_staff.urls')),  # Include Developer Staff URLs
        path('HoD_Maintanance/', include('HoD_Maintanance.urls')),  # Include HoD Maintenance URLs
        path('memberofmaintenance/', include('memberofmaintenance.urls')),
    path('graphicsmember/', include('graphicsmember.urls')),  # Include Graphics Member URLs
    path('hod_of_human_resources/', include('hod_of_human_resources.urls')),
]
