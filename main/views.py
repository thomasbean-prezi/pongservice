from django.shortcuts import get_object_or_404, render

from .models import *


def index(request):
    matches = Match.objects.all()
    results = {}
    for match in matches:
        if match.player1_score > match.player2_score:
            winner = match.player1.name
            loser = match.player2.name
            w = match.player1_score
            l = match.player2_score
        else:
            winner = match.player2.name
            loser = match.player1.name
            w = match.player2_score
            l = match.player1_score
        results[match.id]={"winner":winner, "loser":loser, "l":l, "w":w}
    context = {
        'matches': matches,
        'results': results,
    }
    return render(request, 'main/index.html', context)

def players(request):
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'main/players.html', context)

def fields(request):
    fields = Field.objects.all()
    context = {
        'fields': fields,
    }
    return render(request, 'main/fields.html', context)

def player_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'main/player_detail.html', {'player': player})


