from django.http import HttpResponse
from django.shortcuts import render
from .models import user

# Create your views here..
def addUser(request):
    emp = user(uname='dhwani', uage=21, uemail='d123@gmail.com', ucontact=123456789)
    emp.save()
    return HttpResponse("user added..")

def viewUser(request):
    emp1 = user.objects.all().values_list()
    print(emp1)
    return render(request,'user/view.html',{'user':emp1})

def deleteUser(request):
    emp = user.objects.get(id =1)
    emp.delete()
    return HttpResponse("user deleted..")

def updateUser(request):
   emp = user.objects.get(id =2)
   emp.uname='shreya'
   emp.save()
   return HttpResponse("user updated..") 