# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Book

def index(request):
    context = {
        "books" :Book.objects.all()
    #select * from Book
    }
    Book.objects.create(title="The Count of Monte Cristo", author="Alexandre Dumas", category="Classic")
    Book.objects.create(title="A Tale of Two Cities", author="Charles Dickens", category="Classic")
    Book.objects.create(title="A Raisin in the Sun", author="Lorraine Hansberry", category="Play")
    Book.objects.create(title="Death of a Salesman", author="Arthur Miller", category="Play")
    Book.objects.create(title="Ready Player One", author="Ernest Cline", category="Sci-Fi")
    #book = Book.objects.all()
    #print(book)
    return render(request, 'firstapp/index.html', context)

def books(request):
    #Using ORM
    Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    #insert into books (title, book, created_at, updated_at) values (title, book, now(), now() )
    return redirect('/')