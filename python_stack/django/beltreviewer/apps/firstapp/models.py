from django.db import models
import bcrypt, re

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
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

    def isValidRegistration(self, user_info):
        error_messages = []
        if not user_info['first_name'].isalpha():
            error_messages.append('First name contains non-alpha character(s)')
        if len(user_info['first_name']) < 2:
            error_messages.append('First name is not long enough.')
        if not user_info['last_name'].isalpha():
            error_messages.append('Last name contains non-alpha character(s)')
        if len(user_info['last_name']) < 2:
            error_messages.append('Last name is not long enough.')
        if len(user_info['alias']) < 2:
            error_messages.append('Alias name is not long enough.')
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
            User.objects.create(first_name = user_info['first_name'], last_name = user_info['last_name'], alias = user_info['alias'], email = user_info['email'], password = hashed)
        return error_messages

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=55)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name="books")

class Review(models.Model):
    content = models.TextField(max_length=2000)
    stars = models.IntegerField()
    book = models.ForeignKey(Book, related_name="reviews")
    user = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
