from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
    context = {
        #"leagues": League.objects.filter(sport='baseball')
        #"leagues": League.objects.filter(name__contains="Womens'"),
        #"leagues": League.objects.filter(name__contains="hock"),
        #"leagues": League.objects.exclude(sport="Football"),
        #"leagues": League.objects.exclude(name__contains="Conf"),
        #"leagues": League.objects.filter(name__contains="Atlantic"),
        #"teams": Team.objects.filter(location="Dallas"),
        #"teams": Team.objects.all(),
        #"teams": Team.objects.filter(team_name="Raptors"),
        #"teams": Team.objects.filter(location__contains='City'),
        #"teams": Team.objects.filter(team_name__startswith='T'),
        #"teams": Team.objects.order_by('location'),
        #"teams": Team.objects.order_by("-team_name"),
        #"players": Player.objects.filter(last_name="Cooper"),
        #"players": Player.objects.filter(first_name="Joshua"),
        #"players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
        #"players": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")

                            #Sports ORM2
        #"teams": Team.objects.filter(league = League.objects.filter(name="Atlantic Soccer Conference")),
        #"players": Player.objects.filter(curr_team = Team.objects.filter(team_name="Boston Penguins"))
        #"players": Player.objects.filter(curr_team = Team.objects.filter(league = League.objects.filter(name="International Collegiate Baseball Conference")))
        #"players": Player.objects.filter(last_name = "Lopez").filter(curr_team = Team.objects.filter(league = League.objects.filter(name="American Conference of Amateur Football")))

    }
    return render(request, "firstapp/index.html", context)


def make_data(request):
    team_maker.gen_leagues(10)
    team_maker.gen_teams(50)
    team_maker.gen_players(200)

    return redirect("index")
