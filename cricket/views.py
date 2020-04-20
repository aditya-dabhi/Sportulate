from django.shortcuts import render
from . import simulator

team = [
    'Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab', 'Kolkata Knight Riders',
    'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
]


# Create your views here.
def results(request):
    if request.method == 'POST':
        team1 = request.POST['team1']
        team2 = request.POST['team2']
        result = simulator.sim(team1, team2)
        return render(request, 'cricket/cricresults.html', {
            'teams': [team1, team2],
            'results': [result[0], result[1]]
        })


def home(request):
    context = {
        'team': team
    }
    return render(request, 'cricket/crichome.html', context)
