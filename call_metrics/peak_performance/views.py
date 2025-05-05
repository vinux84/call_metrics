from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User # for registering a user. "User" is built in django module
from django import forms
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html', {})

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST) # getting everything they put in at the signup form
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Something went wrong"))
            return redirect('register')
    else:
        return render(request, 'register.html', {"form":form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['InputUsername']
        password = request.POST['InputPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Wrong Username or Password"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')


