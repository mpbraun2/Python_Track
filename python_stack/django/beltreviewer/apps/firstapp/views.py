from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import get_messages
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User, Book, Author, Review

def index(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, "firstapp/index.html", context)

def register(request):
    user_info = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'alias': request.POST['alias'],
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

    return render(request, "firstapp/success.html")

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

def logout(request):
    request.session.clear()
    messages.success(request, "Successfully logged out")
    return redirect(reverse('index'))

def add_book(request):
    return render(request, "firstapp/add_book.html")

def add_review(request, book_id):
    return render(request, "firstapp/show_book.html")

def show_book(request):
    context = {
        "messages":get_messages(request),
        "reviews":Review.objects.all().order_by('-created_at')[:3], #reverses the order
        "books":Book.objects.all().order_by('title')
    }
    return render(request, "firstapp/show_book.html", context)

def show_users(request):         #this is a test
    context = {
        'users': User.objects.all(),
    }
    return render(request, "firstapp/show_users.html", context)

def delete_user(request, user_id):
    u = User.objects.get(id=user_id)
    u.delete()
    return redirect('/show_users')


def user_profile(request, user_id):
    context = {
        "user":User.objects.get(id=user_id)
    }
    return render(request, "firstapp/user_profile.html", context)

def update_user(request, user_id):
    context = {
        "user":User.objects.get(id=user_id)
    }
    return render(request, "firstapp/update_user.html", context)

def edit_user(request, user_id):
    updated_user = User.objects.get(id=user_id)
    updated_user.first_name = request.POST["first_name"]
    updated_user.last_name = request.POST["last_name"]
    updated_user.alias = request.POST["alias"]
    updated_user.email = request.POST["email"]
    updated_user.save()
    return redirect('/show_users')
