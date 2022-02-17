from django.views.generic import ListView
from django.db.models.query import QuerySet
from django.db import models
from django.shortcuts import render
from .models import Student

# Create your views here.
class StudentList(ListView):
    models = Student
    queryset = Student.objects.all()
    print("details = ",queryset)
    for i in queryset:
        print(i.sname)
    template_name = 'student/list.html'
    context_object_name = 'queryset'