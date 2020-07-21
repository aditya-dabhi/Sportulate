from django.shortcuts import render
from .models import BBTeam
from . import simulator


# Create your views here.
def results(request):
    if request.method == 'POST':
        team1 = request.POST['team1']
        team2 = request.POST['team2']
        result = simulator.sim(team1, team2)
        if BBTeam.objects.filter(name=team1).first().primary_color_name == BBTeam.objects.filter(name=team2).first().primary_color_name:
            back1 = BBTeam.objects.filter(name=team1).first().primary_color_code
            back2 = BBTeam.objects.filter(name=team2).first().secondary_color_code
        else:
            back1 = BBTeam.objects.filter(name=team1).first().primary_color_code
            back2 = BBTeam.objects.filter(name=team2).first().primary_color_code
        return render(request, 'basketball/bbresults.html', {
            'teams': [team1, team2],
            'results': [result[0], result[1]],
            'background_color': [back1, back2]
        })


def home(request):
    context = {
        'teams': BBTeam.objects.all()
    }
    return render(request, 'basketball/bbhome.html', context)
