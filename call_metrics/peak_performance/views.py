from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def register(request):
    if request.method == "POST":
        form = UserCreationForm()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
    else:
        form = UserCreationForm()
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


