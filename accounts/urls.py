from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register',register),
    path('login',log_in),
    path('logout',log_out)
]
