# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    response = "YOU'RE THE MAN NOW DOG!"
    return HttpResponse(response)
