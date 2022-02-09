from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def grouping(request):
    return HttpResponse("group is called..")

def contactUs(request):
    return render(request,'group/contactUs.html')

def index(request):
    return render(request,'group/index.html')

def aboutUs(request):
    return render(request,'group/aboutUs.html')
