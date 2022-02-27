from dataclasses import fields
from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import Module

# Create your views here.

class AddModule(CreateView):
    model = Module
    fields = ['title', 'description', 'technology', 'estimatehours']
    template_name = 'module/add.html'
    success_url = '/module/view/'

class ViewModule(ListView):
    model = Module
    temp = model.objects.all()
    context_object_name = 'temp'
    template_name = 'module/view.html'
    

class DetailModule(DetailView):
    model = Module
    context_object_name = 'temp'
    template_name = 'module/detail.html'

class DeleteModule(DeleteView):
    model = Module
    template_name = 'module/delete.html'
    success_url = '/module/view/'

class UpdateModule(UpdateView):
    model = Module
    fields = ['title', 'description', 'technology', 'estimatehours']
    template_name = 'module/update.html'
    success_url = '/module/view/'
