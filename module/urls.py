from django import views
from django.contrib import admin
from django.urls import path,include

from .views import AddModule,ViewModule,DetailModule,DeleteModule,UpdateModule


urlpatterns = [
  
    path('add/',AddModule.as_view(), name='add_module'),
    path('view/',ViewModule.as_view(), name='view_module'),
    path('<int:pk>/view/',DetailModule.as_view(), name='detail_module'),
    path('<int:pk>/delete/',DeleteModule.as_view(), name='delete_module'),
    path('<int:pk>/update/',UpdateModule.as_view(), name='update_module'),

]