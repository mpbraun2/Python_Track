from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Appointment
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'firstapp/index.html')

def register(request):
    user_info = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
        'dob': request.POST['dob'],
        'password': request.POST['password'],
        'confirm_password': request.POST['confirm_password']
    }
    errors=User.objects.isValidRegistration(user_info)
    if len(errors) == 0:
        messages.success(request, "Success! Welcome, " + user_info['first_name'] + "!")
        return redirect(reverse('success'))
    else:
        for error in errors:
            messages.success(request, error)
        return redirect(reverse('index'))

def success(request):
    context = {
        'appointments': Appointment.objects.all(),
    }
    return render(request, 'firstapp/success.html', context)

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

def add_appointment(request):
    if request.method == "POST":
        Appointment.objects.create(appointment_date=request.POST["appointment_date"], appointment_time=request.POST["appointment_time"], appointment_task=request.POST["appointment_task"], appointment_id=request.POST["appointment_id"])
    return redirect('/success')
    #context = {
        #"appointment":Appointment.objects.all()
    #}
    #return render(request, 'firstapp/success.html', context)

def update_appointment(request, appointment_id):
    updated_appointment = User.objects.get(id=appointment_id)
    updated_appointment.date = request.POST["appointment_date"]
    updated_appointment.time = request.POST["appointment_time"]
    updated_appointment.task = request.POST["appointment_task"]
    updated_appointment.save()
    return redirect('firstapp/success.html')

def delete_appointment(request, appointment_id):
    a_delete = Appointment.objects.get(id=appointment_id)
    a_delete.delete()
    return redirect('firstapp/success.html')
