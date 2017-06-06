Put all steps in this file.

virtualenv djangoEnv

call djangoEnv/scripts/activate   to activate the virtual environment for Django

CREATION
1) create a Django project
    --> django-admin startproject <project name goes here>

2) create an 'apps' folder inside new project
    -->cd <project name goes here>
    -->mkdir apps

3) create dunder-file in apps folder
--> cd apps
-->copy nul __init__.py (double underscores)

4) create an app in the 'apps' folder
--> python ../manage.py startapp <app name here>

5) create urls.py file inside of newly created apps
-->cd <app name goes here>
--> copy nul urls.py


EDITS (IN VISUAL STUDIO CODE)
1) settings.py -> register newly created apps in INSTALLED APPS (settings.py is in main project folder)
    'apps.<appname>',

2) include app urls.py in project urls.py
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.firstapp.urls')),
]


3) create a method in app's views.py
from django.shortcuts import render

def index(request):
    return render(request, 'firstapp/index.html')

4)update the apps urls.py file with route
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
]


If form, add {% csrf_token %} to form.

example: 
{{request.session.name}}    AVOID USING SESSION IF COMPLEX.
<form action="new_user" method = "post">
    {% csrf_token %}
    <input type="text" name = "first_name">
    <input type="submit" value = "submit">
    </form>

    in views in views.py, you will need to update the methods (what comes after the def)
    example: 
    def create(request):
        print (request.method)
        if request.method == "POST"
            print ('*'*50)
            print (request.POST)
            print ('*'*50)
            request.session['name'] = request.POST['first_name']
            return redirect('/')
        else: return redirect('/')

python manage.py makemigrations
python manage.py migrate

rendering a template of HTML(
    def index(request):
    return render(request, 'firstapp/index.html')

request.POST
    Data from POST request
request.GET
    Data from GET request

TO SHOW A USER VARIABLE ON A PAGE
IN VIEWS:
    def create(request):
        if request.method == "POST"
        request.session['name'] = request.POST['first_name']
        return redirect(/)
IN HTML
    {{request.session.name}}


MODELS:

from django.db import models

# Create your models here.
class User(models.Model):     #Class tends to be singular
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField()    #No limit
    created_at = models.DateTimeField(auto_now_add=True)    #will add time at creation once
    updated_at = models.DateTimeField(auto_now=True)        #will add time everytime it updates

if "User" can have many of another class: One to Many Relationship like users to posts: Create a second class in models

class Post(models.Model):djan
    title = models.Charfield(max_length=45)
    message = models.Textfield(max_length=1000)
    user_id = models.ForeignKey(User)    #This connects the class "Post" to class "User" (one to many)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    url(r'^users/(?P<id>)\d+)$', views.show)