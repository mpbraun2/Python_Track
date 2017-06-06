from django.shortcuts import render

import random
VALUES = ["this", "is", "a", "list", "of", "random", "strings"]

def index(request):
    return render(request, 'firstapp/index.html')

def show(request):
    random.shuffle(VALUES)
    print VALUES
    context = {

    }
    #provide the same number of values as those requested
    return render(request, 'firstapp/show.html', context)

def process(request):
    pass
    