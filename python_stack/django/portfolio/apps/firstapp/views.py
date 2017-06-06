# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'firstapp/index.html')

def serve(request):
    return render(request, 'firstapp/serve_testimonials.html')