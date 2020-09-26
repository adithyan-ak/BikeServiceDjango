
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

  path('', views.index, name='index'),
  path('register', views.register, name='register'),
  path('dashboard', views.dashboard, name='dashbboard'),
  path('service', views.service, name='service'),
  path('login', views.Login, name='login'),
  path('logout', views.logout, name='logout'),
]