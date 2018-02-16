import json
import datetime

from django.http import HttpResponse, JsonResponse
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
    print results
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

def api_players(request):
    if request.method == "GET":
        players = Player.objects.all()
        data = []
        for player in players:
            data.append({"id": player.id, "name": player.name})
        return JsonResponse({"players": data})
    elif request.method == "POST":
        data = json.loads(request.body)
        player = Player.objects.create(name=data["name"])
        return JsonResponse({"id": player.id, "name": player.name})

def api_fields(request):
    if request.method == "GET":
        fields = Field.objects.all()
        data = []
        for field in fields:
            data.append({"id": field.id, "name": field.name})
        return JsonResponse({"fields": data})
    elif request.method == "POST":
        data = json.loads(request.body)
        field = Field.objects.create(name=data["name"])
        return JsonResponse({"id": field.id, "name": field.name})

def api_matches(request):
    if request.method == "GET":
        matches = Match.objects.all()
        data = []
        for match in matches:
            data.append({"id": match.id, "date_and_time": match.date_and_time,
                         "player1": match.player1.name, "player2": match.player2.name,
                         "player1_score": match.player1_score, "player2_score": match.player2_score,
                         "field": match.field.name})
        return JsonResponse({"matches": data})
    elif request.method == "POST":
        data = json.loads(request.body)
        #if the player entered already exists, use that object. If not, make a new one and use that
        #some kind of try catch block would be good here. Try to "get(name=data["player1"])" if that throws an exception
        #then make a new player and use that

        #bad part about this is that it has to be EXACTLY the same name
        #also cannot identify by id number
        #there is definitely a better way to do this. Maybe some django magic?
        if Player.objects.filter(name=data["player1"]).exists():
            p1 = Player.objects.get(name=data["player1"])
        else:
            p1 = Player.objects.create(name=data["player1"])

        if Player.objects.filter(name=data["player2"]).exists():
            p2 = Player.objects.get(name=data["player2"])
        else:
            p2 = Player.objects.create(name=data["player2"])

        if Field.objects.filter(name=data["field"]).exists():
            field = Field.objects.get(name=data["field"])
        else:
            field = Field.objects.create(name=data["field"])
        match = Match.objects.create(date_and_time=datetime.datetime.now(),player1=p1,player2=p2,
                                     player1_score=data["player1_score"],player2_score=data["player2_score"],field=field)
        return JsonResponse({"id": match.id, "date_and_time": match.date_and_time,
                             "player1": match.player1.name, "player2": match.player2.name,
                             "player1_score": match.player1_score, "player2_score": match.player2_score,
                             "field": match.field.name})

def api_player_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return JsonResponse({"id": player.id, "name": player.name})

def api_field_detail(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    return JsonResponse({"id": field.id, "name": field.name})

def api_match_detail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return JsonResponse({"id": match.id, "date_and_time": match.date_and_time,
                         "player1": match.player1.name, "player2": match.player2.name,
                         "player1_score": match.player1_score, "player2_score": match.player2_score,
                         "field": match.field.name})

