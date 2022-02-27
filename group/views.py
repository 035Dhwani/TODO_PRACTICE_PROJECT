from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here..
def grouping(request):
    return HttpResponse("group is called..")

def contactUs(request):
    context={
        'contact_name': ["dhwani", "shreya", "abhi", "deep", "sweta", "payal", "keval"],
    }
    return render(request,'group/contactUs.html',context)

def index(request):
    context={
        'name': 'FLIPKART',
    }
    return render(request,'group/index.html',context)

def aboutUs(request):
    context={
        'isActive': 'False',
        'age': 20
    }
    return render(request,'group/aboutUs.html',context)
