from django.http import HttpResponse
from django.shortcuts import render

# Create your views here..
def addproduct(request):
    print("addproduct app ")
    return HttpResponse("add product called..")

def viewproduct(request):
    return HttpResponse("view product called..")
def productpage(request):
    return render(request, 'product/productpage.html')