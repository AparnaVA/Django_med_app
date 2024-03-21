"""
URL configuration for examproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from medical_store import views

urlpatterns = [
    path('',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('create/',views.medicine_create,name='createmedicine'),
    path('home/',views.welcome,name='home'),
    path('retrieve/',views.medicine_read,name='retrievemedicine'),
    path('logout/', views.logout_view,name='logout'),
    path('update/<int:pk>/',views.medicine_update,name='updatemedicine'),
    path('delete/<int:pk>',views.medicine_delete,name='deletemedicine'),
    path('search/', views.search, name='search'),
    path('medicineapi/',include('medicineapi.urls')),
    
]
