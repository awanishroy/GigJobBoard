"""
URL configuration for CurdApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from GigApp.page.Candidate import views

urlpatterns = [

    path('', views.home, name='admin.home'), # Default home page 

    # path('admin/', admin.site.urls),


    # Here is aur all api's Endpoint
    path('api/', include('GigApp.apis.Candidate.urls')),

    # Admin Panel Urls
    path('admin/', include('GigApp.page.Auth.urls')),
    path('admin/', include('GigApp.page.Candidate.urls')),
    path('admin/', include('GigApp.page.Company.urls')),
    path('admin/', include('GigApp.page.Home.urls')),

]