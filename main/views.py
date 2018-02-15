from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

from .models import Player

def index(request):
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'main/index.html', context)

def player_detail(request, player_id):
    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'main/detail.html', {'player': player})
    #return HttpResponse("You're looking at palyer %s." % player_id)


