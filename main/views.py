from django.shortcuts import render

from .models import Player

def index(request):
    players = Player.objects.all()
    context = {
        'players': players, # must pyhton dictionary
    }
    return render(request, 'main/index.html', context)


