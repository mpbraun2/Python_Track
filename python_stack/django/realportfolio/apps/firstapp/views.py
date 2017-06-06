# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'firstapp/index.html')

def testimonials(request):
    return render(request, 'firstapp/testimonials.html')

def aboutme(request):
    return render(request, 'firstapp/aboutme.html')

def projects(request):
    return render(request, 'firstapp/projects.html')
