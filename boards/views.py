from django.shortcuts import render , get_object_or_404
# from django.http import Http404
from .models import Board


def home(response):
    boards = Board.objects.all()
    return render(response, 'home.html', {'boards':boards})

def board_topics(response, id):
    board = get_object_or_404(Board,id=id)
    return render(response, 'topics.html', {'board' : board})
