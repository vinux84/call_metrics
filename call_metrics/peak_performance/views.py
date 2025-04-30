from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html', {})

def register(request):
    form = UserCreationForm()
    return render(request, 'register.html', {"form":form})

def login(request):
    return render(request, 'login.html', {})


