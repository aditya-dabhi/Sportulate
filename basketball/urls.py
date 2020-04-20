from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bb-home'),
    path('results/', views.results, name='bb-results')
]