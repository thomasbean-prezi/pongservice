from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Player
from .models import Match


def index(request):
    matches = Match.objects.all()
    context = {
        'matches': matches,
    }
    return render(request, 'main/index.html', context)

def players(request):
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'main/players.html', context)

def player_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'main/player_detail.html', {'player': player}) # i think i should rename player_detail.html to player_detail.html


