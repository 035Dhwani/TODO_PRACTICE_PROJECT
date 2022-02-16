from django import views
from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('add/', views.addUser),
    path('view/',views.viewUser),
    path('delete/',views.deleteUser),
    path('update/',views.updateUser),
    

]
