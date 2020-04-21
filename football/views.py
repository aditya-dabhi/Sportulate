from django.shortcuts import render
from . import simulator
team = [
    'Arsenal', 'Aston Villa', 'AFC Bournemouth', 'Brighton and Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace',
    'Everton', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City',
    'Sheffield United', 'Southampton', 'Tottenham Hotspur', 'Watford', 'West Ham United', 'Wolverhampton Wanderers'
]

colour_code = {
    'Arsenal': ['red', 'rgb(239,1,7)', 'yellow', 'rgb(241, 247, 59)'],
    'Aston Villa': ['maroon', 'rgb(103,14,54)', 'blue', 'rgb(149,191,229)'],
    'AFC Bournemouth': ['red', 'rgb(181,14,18)', 'black', 'rgb(0,0,0)'],
    'Brighton and Hove Albion': ['blue', 'rgb(0,87,184)', 'yellow', 'rgb(255,205,0)'],
    'Burnley': ['maroon', 'rgb(108,29,69)', 'blue', 'rgb(153,214,234)'],
    'Chelsea': ['blue', 'rgb(3, 70, 148)', 'black', 'rgb(0,0,0)'],
    'Crystal Palace': ['blue', 'rgb(27, 69, 143)', 'red', 'rgb(196, 18, 46)'],
    'Everton': ['blue', 'rgb(39,68,136)', 'pink', 'rgb(255, 89, 147)'],
    'Leicester City': ['blue', 'rgb(0,83,160)', 'gold', 'rgb(253,190,17)'],
    'Liverpool': ['red', 'rgb(200,16,46)', 'green', 'rgb(0,178,169)'],
    'Manchester City': ['blue', 'rgb(108,171,221)', 'purple', 'rgb(124, 37, 179)'],
    'Manchester United': ['red', 'rgb(218 41 28)', 'black', 'rgb(6,25,34)'],
    'Newcastle United': ['black', 'rgb(45 41 38)', 'blue', 'rgb(45, 82, 214)'],
    'Norwich City': ['yellow', 'rgb(255, 242, 0)', 'green', 'rgb(0, 166, 80)'],
    'Sheffield United': ['red', 'rgb(238,39,55)', 'black', 'rgb(13,23,26)'],
    'Southampton': ['red', 'rgb(215,25,32)', 'black', 'rgb(19,12,14)'],
    'Tottenham Hotspur': ['gray', 'rgb(216, 219, 230)', 'blue', 'rgb(19,34,87)'],
    'Watford': ['yellow', 'rgb(251,238,35)', 'black', 'rgb(18,17,12)'],
    'West Ham United': ['maroon', 'rgb(122,38,58)', 'blue', 'rgb(27,177,231)'],
    'Wolverhampton Wanderers': ['orange', 'rgb(255, 125, 3)', 'black', 'rgb(35,31,32)'],
    'Draw': ['gray', 'rgb(216, 219, 230)', 'green', 'rgb(120,190,32)']
}


# Create your views here.
def results(request):
    if request.method == 'POST':
        team1 = request.POST['team1']
        team2 = request.POST['team2']
        result = simulator.sim(team1, team2)
        if colour_code[team1][0] == colour_code[team2][0]:
            back1 = colour_code[team1][1]
            back2 = colour_code[team2][3]
        else:
            back1 = colour_code[team1][1]
            back2 = colour_code[team2][1]
        if colour_code['Draw'][1] == back1 or colour_code['Draw'][1] == back2:
            back3 = colour_code['Draw'][3]
        else:
            back3 = colour_code['Draw'][1]
        return render(request, 'football/footresults.html', {
            'teams': [team1, team2, 'Draw'],
            'results': [result[0], result[1], result[2]],
            'background_color': [back1, back2, back3]
        })


def home(request):
    context = {
        'team': team
    }
    return render(request, 'football/foothome.html', context)
