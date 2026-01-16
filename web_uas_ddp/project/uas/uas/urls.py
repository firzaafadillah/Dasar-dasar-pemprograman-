"""
URL configuration for uas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from authentication import views

urlpatterns = [
    path('', views.dashboard_view, name = 'dashboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('authentication.urls')),
    path('', views.beranda_view, name='beranda'),
    path('berhitung/', views.berhitung_view, name='berhitung'),
    path('bilangan/', views.bilangan_view, name='bilangan'),
    path('geometri/', views.geometri_view, name='geometri'),
]

