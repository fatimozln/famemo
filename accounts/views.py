from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_library
from django.contrib.auth import logout as logout_library
from profiles import models
from .models import MyUser
from .forms import LoginForm, SignupForm


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.clean()
            password = cd['password']
            password_confirmation = cd['password_confirmation']
            username = cd['username']

            if password != password_confirmation:
                return HttpResponse('Password confirm is invalid .')
            try:
                user_exists = MyUser.objects.get(username=username)
            except MyUser.DoesNotExist:
                user_exists = False
            if user_exists:
                return HttpResponse('username is invalid .')
            else:
                user = MyUser.objects.create_user(
                    username=username, password=password)
                return redirect('accounts:login')

    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.clean()
            user_name = cd['username']
            password = cd['password']
            user = authenticate(username=user_name, password=password)
            if user:
                if user.status != 'deactive':
                    login_library(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('user is Deactive .')
            else:
                return HttpResponse('Dose Not Exists .')
    return render(request, 'accounts/login1.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        logout_library(request)
        return redirect('articles:list')
