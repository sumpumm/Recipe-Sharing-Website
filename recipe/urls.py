from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
   path('',index),
   # path('logout/',index),
   path('create',create),
   path('recipe/categories',category),
   path('recipe/<pk>',view_recipe),
   path('recipe/edit/<pk>',edit),
   path('recipe/delete/<pk>',delete),
   path('category/<pk>',category_recipe),
   path('create_category',create_category),
]
