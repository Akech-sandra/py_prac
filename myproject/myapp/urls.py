from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from myapp import views
from .import views
from .views import *

urlpatterns = [
    path('', views.details, name='details'),
]
