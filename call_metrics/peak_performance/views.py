from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User # for registering a user. "User" is built in django module
from django import forms
from .models import Project
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, ProjectForm
from django.contrib.auth.decorators import login_required

def home(request):
    projects = Project.objects.all().order_by('-date_updated')
    return render(request, 'home.html', {'projects':projects})

def project(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'project.html', {'project': project})

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
            messages.success(request, "Wrong Username or Password")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'user_profile.html', {})
    else:
        messages.success(request, "You must be logged in to access that page")
        return redirect('home')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Successfully Updated Profile") 
            return redirect('user_profile')
        return render(request, "update_user.html", {'user_form':user_form})
    else:
        messages.success(request, "You must be logged in to access that page")
        return redirect('home')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        # did they fill out the form? 
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Password Updated")
                login(request, current_user)
                return redirect('user_profile')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to access that page")
        return redirect('home')

'''  
def add_project(request):
    if request.user.is_authenticated:
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            new_project = project_form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            messages.success(request, f'Project "{new_project.name}" created successfully!')
        return render(request, "add_project.html", {'project_form':project_form})
    else:
        messages.success(request, "You must be logged in to access that page")
        return redirect('home')
'''

@login_required(login_url='login/')
def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            add_project = form.save(commit=False)
            add_project.user = request.user
            add_project.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {'form':form})





        

