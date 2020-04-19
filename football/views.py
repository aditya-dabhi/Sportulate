from django.shortcuts import render

team = [
    'Arsenal', 'Aston Villa', 'AFC Bournemouth', 'Brighton and Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace',
    'Everton', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City',
    'Sheffield United', 'Southampton', 'Tottenham Hotspur', 'Watford', 'West Ham United', 'Wolverhampton Wanderers'
]


# Create your views here.
def home(request):
    context = {
        'team': team
    }
    return render(request, 'football/foothome.html', context)
