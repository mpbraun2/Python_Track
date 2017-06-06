# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Book

def index(request):
    Book.objects.create(title="The Count of Monte Cristo", author="Alexandre Dumas", published_date="1844", category="classic", in_print='True')
    Book.objects.create(title="A Tale of Two Cities", author="Charles Dickens", published_date="1859", category="classic", in_print='False')
    Book.objects.create(title="A Raisin in the Sun", author="Lorraine Hansberry", published_date="1959", category="play", in_print='True')
    Book.objects.create(title="Death of a Salesman", author="Arthur Miller", published_date="1949", category="play", in_print='False')
    Book.objects.create(title="Ready Player One", author="Ernest Cline", published_date="2011", category="Sci-Fi", in_print='True')
    book = Book.objects.all()
    print(book)
    return render(request, 'firstapp/index.html')
