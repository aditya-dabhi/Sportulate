from django.shortcuts import render
from . import simulator
team = [
    'Arsenal', 'Aston Villa', 'AFC Bournemouth', 'Brighton and Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace',
    'Everton', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City',
    'Sheffield United', 'Southampton', 'Tottenham Hotspur', 'Watford', 'West Ham United', 'Wolverhampton Wanderers'
]


# Create your views here.
def results(request):
    if request.method == 'POST':
        team1 = request.POST['team1']
        team2 = request.POST['team2']
        result = simulator.sim(team1, team2)
        return render(request, 'football/footresults.html', {
            'teams': [team1, team2, 'Draw'],
            'results': [result[0], result[1], result[2]]
        })


def home(request):
    context = {
        'team': team
    }
    return render(request, 'football/foothome.html', context)
