from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
class UserLogin(LoginView):
    template_name = 'core/login.html'

class Logout(LogoutView):
    pass
