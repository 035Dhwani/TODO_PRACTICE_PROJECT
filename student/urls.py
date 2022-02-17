from django.contrib import admin
from django.urls import path,include
from .views import StudentList

urlpatterns = [
   
   path('view/',StudentList.as_view())

]
