from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.messages import get_messages
from django.contrib import messages
import re, bcrypt
from django.core.urlresolvers import reverse
from .models import User
#from django.db.models import Count

def index(request):
    return render(request, 'firstapp/index.html')

def register(request):
    user_info = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'confirm_password': request.POST['confirm_password'],
        #'date_birth': request.POST['date_birth'],
    }
    errors = User.objects.isValidRegistration(user_info)
    if len(errors) == 0:
        messages.success(request, "Success! Welcome, " + user_info['first_name'] + "!")
        return redirect(reverse('appointments'))
    else:
        for error in errors:
            messages.success(request, error)    #error stands for the value in the index (set on previous line)
        return redirect(reverse('index'))

def appointments(request):
    return render(request, 'firstapp/appointments.html')

def login(request):
    user_info = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }
    errors = User.objects.UserExistsLogin(user_info)
    if User.objects.UserExistsLogin(user_info):
        for error in errors:
            messages.success(request, error)
        return redirect(reverse('appointmets'))
    else:
        for error in errors:
            messages.success(request, error)
        return redirect(reverse('index'))

def log_out_user(request):
    request.session.clear()
    messages.success(request, "Successfully logged out")
    return redirect('/')
    