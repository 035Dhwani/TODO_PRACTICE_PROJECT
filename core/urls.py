
from django.contrib import admin
from django.urls import path,include
from .views import UserLogin,Logout

urlpatterns = [
   
   path('login/',UserLogin.as_view(), name="login"),
   path('logout/',Logout.as_view(), name="logout"),
]