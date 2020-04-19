from django.shortcuts import render

team = [
    'Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab', 'Kolkata Knight Riders',
    'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
]
# Create your views here.
def home(request):
    context = {
        'team': team
    }
    return render(request, 'cricket/crichome.html',context)