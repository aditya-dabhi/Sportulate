from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cricket-home'),
    path('results/', views.results, name='cric-results')
]