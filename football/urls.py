from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='football-home'),
    path('results/', views.results, name='football-results')
]