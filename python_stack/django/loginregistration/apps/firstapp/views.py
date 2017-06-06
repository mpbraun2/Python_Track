from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'firstapp/index.html')

def register(request):
    user_info = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'confirm_password': request.POST['confirm_password']
    }
    errors=User.objects.isValidRegistration(user_info)
    if len(errors) == 0:
        messages.success(request, "Success! Welcome, " + user_info['first_name'] + "!")
        return redirect(reverse('success'))
    else:
        for error in errors:
            messages.success(request, error)    #error stands for the value in the index (set on previous line)
        return redirect(reverse('index'))

def success(request):
    return render(request, 'firstapp/success.html')

def login(request):
    user_info = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }
    errors = User.objects.UserExistsLogin(user_info)
    if User.objects.UserExistsLogin(user_info):
        for error in errors:
            messages.success(request, error)
        return redirect(reverse('success'))
    else:
        for error in errors:
            messages.success(request, error)
        return redirect(reverse('index'))
