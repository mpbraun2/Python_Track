# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import User, Message, Comment
def index(request):
    User.objects.create(first_name="Mike", last_name="Dumas", email="Mdumas@email.com", password="classic")
    User.objects.create(first_name="Greg", last_name="Dickens", email="Gdickens@gmail.com", password="newword")
    User.objects.create(first_name="Andy", last_name="Hansberry", email="Ahansberry@gmail.com", password="play")
    user = User.objects.all()
    print(user)
    Message.objects.create(message="Hello! This is my message", user_id=1)
    Message.objects.create(message="Hello! This is my message as well", user_id=2)
    Message.objects.create(message="Hello! This is my message, too", user_id=3)
    message = Message.objects.all()
    print(message)
    Comment.objects.create(comment="What a novel concept", user_id=1, message_id=2)
    Comment.objects.create(comment="Can you believe it?", user_id=2, message_id=3)
    Comment.objects.create(comment="Woohoo", user_id=3, message_id=1)
    comment = Comment.objects.all()
    print(comment)
    return render(request, 'firstapp/index.html')
