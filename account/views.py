from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import *


class HomeView(TemplateView):
    template_name = 'account/home.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')
    
    
class LoginView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')
    

# i want to make logout view without template
# views.py


class LogoutView(LogoutView):
    next_page = reverse_lazy('home')








