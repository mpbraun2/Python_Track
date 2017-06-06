from django.shortcuts import render
from datetime import datetime

def index(request):
    date = datetime.now().date()
    time = datetime.now().time()
    context = {
        "datetime" : [
            {"date" : date},
            {"time" : time},
        ]
    }
    return render(request, 'firstapp/index.html', context)
