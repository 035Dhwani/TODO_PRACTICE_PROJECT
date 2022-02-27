from django import views
from django.contrib import admin
from django.urls import path
from .views import CreateTicket,DeleteTicket,UpdateTicket
from ticket import views


urlpatterns = [

    path('add/',CreateTicket.as_view()),
    path('view/',views.index),
    path('<pk>/delete/',DeleteTicket.as_view()),
    path('<pk>/update/',UpdateTicket.as_view()),
    
]

 
