from django.shortcuts import render
from . import simulator

team = [
    'Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers',
    'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons', 'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers','Los Angeles Clippers',
    'Los Angeles Lakers', 'Memphis Grizzlies', 'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves','New Orleans Pelicans',
    'New York Knicks', 'Oklahoma City Thunder', 'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns','Portland Trail Blazers',
    'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors', 'Utah Jazz', 'Washington Wizards'
]

colour_code = {
    'Atlanta Hawks': ['red', 'rgb(225,68,52)', 'black', 'rgb(38,40,42)'],
    'Boston Celtics': ['green', 'rgb(0,122,51)', 'gold', 'rgb(139,111,78)'],
    'Brooklyn Nets': ['black', 'rgb(0,0,0)', 'gray', 'rgb(214,212,213)'],
    'Charlotte Hornets': ['teal', 'rgb(0,120,140)', 'purple', 'rgb(29,17,96)'],
    'Chicago Bulls': ['red', 'rgb(206,17,65)', 'black', 'rgb(6,25,34)'],
    'Cleveland Cavaliers': ['maroon', 'rgb(134,0,56)', 'gold', 'rgb(253,187,48)'],
    'Dallas Mavericks': ['blue', 'rgb(0,83,188)', 'silver', 'rgb(187,196,202)'],
    'Denver Nuggets': ['blue', 'rgb(13,34,64)', 'yellow', 'rgb(255,198,39)'],
    'Detroit Pistons': ['red', 'rgb(200,16,46)', 'blue', 'rgb(29,66,138)'],
    'Golden State Warriors': ['blue', 'rgb(29,66,138)', 'yellow', 'rgb(255,199,44)'],
    'Houston Rockets': ['red', 'rgb(206,17,65)', 'black', 'rgb(6,25,34)'],
    'Indiana Pacers': ['yellow', 'rgb(253,187,48)', 'blue', 'rgb(0,45,98)'],
    'Los Angeles Clippers': ['blue', 'rgb(29,66,148)', 'red', 'rgb(200,16,46)'],
    'Los Angeles Lakers': ['gold', 'rgb(253,185,39)', 'purple', 'rgb(85,37,130)'],
    'Memphis Grizzlies': ['blue', 'rgb(93,118,169)', 'gray', 'rgb(112,114,113)'],
    'Miami Heat': ['red', 'rgb(152,0,46)', 'blue', 'rgb(65,182,230)'],
    'Milwaukee Bucks': ['green', 'rgb(0,71,27)', 'cream', 'rgb(240,235,210)'],
    'Minnesota Timberwolves': ['blue', 'rgb(12,35,64)', 'green', 'rgb(120,190,32)'],
    'New Orleans Pelicans': ['blue', 'rgb(0,22,65)', 'red', 'rgb(225,58,62)'],
    'New York Knicks': ['orange', 'rgb(245,132,38)', 'blue', 'rgb(0,107,182)'],
    'Oklahoma City Thunder': ['blue', 'rgb(0,125,195)', 'orange', 'rgb(239,59,36)'],
    'Orlando Magic': ['blue', 'rgb(0,125,197)', 'silver', 'rgb(196,206,211)'],
    'Philadelphia 76ers': ['blue', 'rgb(0,107,182)', 'red', '(237,23,76)'],
    'Phoenix Suns': ['purple', 'purple(29,17,96)', 'orange', 'rgb(229,95,32)'],
    'Portland Trail Blazers': ['red', 'rgb(224,58,62)', 'black', 'rgb(6,25,34)'],
    'Sacramento Kings': ['purple', 'rgb(91,43,130)', 'gray', 'rgb(99,113,122)'],
    'San Antonio Spurs': ['black', 'rgb(6,25,34)', 'silver', 'rgb(196,206,211)'],
    'Toronto Raptors': ['red', 'rgb(206,17,65)', 'black', 'rgb(6,25,34)'],
    'Utah Jazz': ['blue', 'rgb(0,43,92)', 'green', 'rgb(0,71,27)'],
    'Washington Wizards': ['blue', 'rgb(0,43,92)', 'red', 'rgb(227,24,55)']
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
        return render(request, 'basketball/bbresults.html', {
            'teams': [team1, team2],
            'results': [result[0], result[1]],
            'background_color': [back1, back2]
        })


def home(request):
    context = {
        'team': team
    }
    return render(request, 'basketball/bbhome.html', context)
