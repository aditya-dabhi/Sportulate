from django.shortcuts import render
from . import simulator
from .models import CricTeam

team = [
    'Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab', 'Kolkata Knight Riders',
    'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
]

colour_code = {
    'Chennai Super Kings': ['yellow', 'rgb(255,255,60)', 'blue', 'rgb(0,139,233)'],
    'Delhi Capitals': ['blue', 'rgb(0,139,233)', 'red', 'rgb(239,27,35)'],
    'Kings XI Punjab': ['red', 'rgb(237,27,36)', 'gray', 'rgb(220,221,223)'],
    'Kolkata Knight Riders': ['purple', 'rgb(46,8,84)', 'gold', 'rgb(179,161,35)'],
    'Mumbai Indians': ['blue', 'rgb(0,75,160)', 'gold', 'rgb(209,171,62)'],
    'Rajasthan Royals': ['pink', 'rgb(255,153,219)', 'blue', 'rgb(37,74,165)'],
    'Royal Challengers Bangalore': ['red', 'rgb(236,28,36)', 'black', 'rgb(43,42,41)'],
    'Sunrisers Hyderabad': ['orange', 'rgb(255,130,42)', 'black', 'rgb(0,0,0)']
}


# Create your views here.
def results(request):
    if request.method == 'POST':
        team1 = request.POST['team1']
        team2 = request.POST['team2']
        result = simulator.sim(team1, team2)
        if CricTeam.objects.filter(name=team1).first().primary_color_name == CricTeam.objects.filter(
                name=team2).first().primary_color_name:
            back1 = CricTeam.objects.filter(name=team1).first().primary_color_code
            back2 = CricTeam.objects.filter(name=team2).first().secondary_color_code
        else:
            back1 = CricTeam.objects.filter(name=team1).first().primary_color_code
            back2 = CricTeam.objects.filter(name=team2).first().primary_color_code
        return render(request, 'basketball/bbresults.html', {
            'teams': [team1, team2],
            'results': [result[0], result[1]],
            'background_color': [back1, back2]
        })


def home(request):
    context = {
        'teams': CricTeam.objects.all()
    }
    return render(request, 'cricket/crichome.html', context)
