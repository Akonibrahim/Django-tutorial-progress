from django.shortcuts import render
from .models import Board

def home(response):
    boards = Board.objects.all()
    return render(response, 'home.html', {'boards':boards})
