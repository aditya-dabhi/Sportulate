from django.shortcuts import render
from .models import FootballTeams
from . import simulator


# Create your views here.
def results(request):
    if request.method == 'POST':
        team1 = request.POST['team1']
        team2 = request.POST['team2']
        result = simulator.sim(team1, team2)
        if FootballTeams.objects.filter(name=team1).first().primary_color_name == FootballTeams.objects.filter(name=team2).first().primary_color_name:
            back1 = FootballTeams.objects.filter(name=team1).first().primary_color_code
            back2 = FootballTeams.objects.filter(name=team2).first().secondary_color_code
        else:
            back1 = FootballTeams.objects.filter(name=team1).first().primary_color_code
            back2 = FootballTeams.objects.filter(name=team2).first().primary_color_code
        if FootballTeams.objects.filter(name='Draw').first().primary_color_code == back1 or FootballTeams.objects.filter(name='Draw').first().primary_color_code == back2:
            back3 = FootballTeams.objects.filter(name='Draw').first().secondary_color_code
        else:
            back3 = FootballTeams.objects.filter(name='Draw').first().primary_color_code
        return render(request, 'football/footresults.html', {
            'teams': [team1, team2, 'Draw'],
            'results': [result[0], result[1], result[2]],
            'background_color': [back1, back2, back3]
        })


def home(request):
    context = {
        'teams': FootballTeams.objects.all()
    }
    return render(request, 'football/foothome.html', context)
