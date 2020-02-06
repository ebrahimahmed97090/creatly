"""Creatly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from users import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^prices/', views.prices, name='prices'),
    url(r'^about/', views.about, name='about'),
    url(r'^service/', views.services, name='services'),
    url(r'^reg/', views.registration, name='reg'),
    url(r'^example/', views.example, name='example'),
    url(r'^Uwl/', views.UWl, name='User_Wlist'),
    url(r'^users/', include('users.urls')),
    url(r'^/', include('users.urls'))
]
