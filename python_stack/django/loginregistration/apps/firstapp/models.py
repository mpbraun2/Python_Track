from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
import re


EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def isValidRegistration(self, user_info):
        error_messages=[]
        if not user_info['first_name'].isalpha():
            error_messages.append('First name contains non-alpha character(s)')
        if len(user_info['first_name']) < 2:
            error_messages.append('First name is not long enough.')
        if not user_info['last_name'].isalpha():
            error_messages.append('Last name contains non-alpha character(s)')
        if len(user_info['last_name']) < 2:
            error_messages.append('Last name is not long enough.')
        if not EMAIL_REGEX.match(user_info['email']):
            error_messages.append('Email is not a valid email!')
        if len(user_info['password']) < 8:
            error_messages.append('Password is not long enough.')
        if user_info['password'] != user_info['confirm_password']:
            error_messages.append('Password match not confirmed.')
        if User.objects.filter(email=user_info['email']):
            error_messages.append("This email already exists in our database.")
        if len(error_messages) == 0:
            hashed = bcrypt.hashpw(user_info['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name = user_info['first_name'], last_name = user_info['last_name'], email = user_info['email'], password = hashed)
        return error_messages

    def UserExistsLogin(self, user_info):
        error_messages=[]
        if User.objects.filter(email = user_info['email']):
            hashed = User.objects.get(email = user_info['email']).password
            hashed = hashed.encode('utf-8')
            password = user_info['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                error_messages.append("Success! Welcome, " + User.objects.get(email = user_info['email']).first_name + "!")
            else:
                error_messages.append("Unsuccessful login. Incorrect password.")
        else:
            error_messages.append("Unsuccessful login. Your email is incorrect.")
        return error_messages


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    #if second class, add user_id = models.ForiegnKey(User) and make sure to import under views