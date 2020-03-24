"""Finesystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from FineSystemapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home ,name='Home'),
    path('Fine/', views.Fine_Apply, name='Fine_Apply'),
    path('Rule/',views.My_rules,name='My_rules'),
    path('Add_Rules/',views.Add_Rules ,name='Add_Rules'),
    path('FU/',views.FU , name='FU'),
    path('About/',views.About,name='About'),
]
