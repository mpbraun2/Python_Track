from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import get_messages
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User, Appointment

def index(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, "firstapp/index.html", context)

def register(request):
    user_info = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'date_of_birth': request.POST['date_of_birth'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'confirm_password': request.POST['confirm_password'],
    }
    errors = User.objects.isValidRegistration(user_info)
    if len(errors) == 0:
        messages.success(request, "Success! Welcome, " + user_info['first_name'] + "!")
        return redirect(reverse('firstapp/appointments'))
    else:
        for error in errors:
            messages.success(request, error)
        return redirect(reverse('index'))

def appointments(request):

    return render(request, "firstapp/appointments.html")

def login(request):
    user_info = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }
    errors = User.objects.UserExistsLogin(user_info)
    if User.objects.UserExistsLogin(user_info):
        for error in errors:
            messages.success(request, error)
        return redirect('/')
    else:
        for error in errors:
            messages.success(request, error)
        return redirect(reverse('index'))

def logout(request):
    request.session.clear()
    messages.success(request, "Successfully logged out")
    return redirect(reverse('index'))

def edit_appointment(request, user_id):
    updated_appointment = User.objects.get(id=user_id)
    updated_appointment.task = request.POST["task"]
    updated_appointment.date = request.POST["date"]
    updated_appointment.time = request.POST["time"]
    updated_appointment.save()
    return redirect('firstapp/appointments')

def add_appointment(request, user_id):
    if request.method == "POST":
        Appointment.objects.create(task=request.POST['task'], date=request.POST['date'], time=request.POST['time'], user=User.objects.get(id=user_id))
    return redirect('firstapp/appointments')
