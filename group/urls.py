from django.contrib import admin
from django.urls import path,include
from group import views
urlpatterns = [
   path('add/',views.grouping),
   path('contactUs/',views.contactUs),
   path('aboutUs/',views.aboutUs),
   path('',views.index),
]
