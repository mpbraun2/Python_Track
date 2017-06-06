from django.shortcuts import render, redirect


def index(request):
    return render (request, 'firstapp/index.html')

def show(request):
    if 'queue' in request.session:
        request.session.pop('queue')
    request.session['showall'] = {
        "blue": '../static/firstapp/images/donatello.jpg',
        "orange": '../static/firstapp/images/michelangelo.jpg',
        "red": '../static/firstapp/images/raphael.jpg',
        "purple": '../static/firstapp/images/leonardo.jpg'
    }
    session_hold = request.session['showall']
    return render(request, 'firstapp/show.html', session_hold)


def showcolor(request, color):
    if 'showall' in request.session:
        request.session.pop('showall')
    if color == "blue":
        context = {
            'color': '../../static/firstapp/images/donatello.jpg'
        }
    elif color == "orange":
        context = {
            'color': '../../static/firstapp/images/michelangelo.jpg'
        }
    elif color == "red":
        context = {
            'color': '../../static/firstapp/images/raphael.jpg'
        }
    elif color == "purple":
        context = {
            'color': '../../static/firstapp/images/leonardo.jpg'
        }
    else:
        context = {
            'color': '../../static/firstapp/images/notapril.jpg'
        }

    return render(request, 'firstapp/show.html', context)
