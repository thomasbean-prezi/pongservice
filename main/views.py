import json
import datetime


from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_http_methods

from .models import *


def index(request):
    matches = Match.objects.all()
    results = []
    for match in matches:
        if match.player1_score > match.player2_score:
            winner_name = match.player1.name
            winner_id = match.player1.id
            loser_name = match.player2.name
            loser_id = match.player2.id
            winner_score = match.player1_score
            loser_score = match.player2_score
        else:
            winner_name = match.player2.name
            winner_id = match.player2.id
            loser_name = match.player1.name
            loser_id = match.player1.id
            winner_score = match.player2_score
            loser_score = match.player1_score
        results.append({
            "id": match.id,
            "date": match.date_and_time,
            "winner": {
                "id": winner_id,
                "name": winner_name,
                "score": winner_score,
            },
            "loser": {
                "id": loser_id,
                "name": loser_name,
                "score": loser_score,
            },
            "field": {
                "id": match.field.id,
                "name": match.field.name,
            }
        })
    context = {
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


@require_http_methods(['GET', 'POST'])
def api_players(request):
    if request.method == "GET":
        players = Player.objects.all()
        data = [{"id": player.id, "name": player.name} for player in players]
        return JsonResponse({"players": data})
    else:
        data = json.loads(request.body)
        player = Player.objects.create(name=data["name"])
        return JsonResponse({
            "id": player.id,
            "name": player.name
        })


@require_http_methods(['GET', 'POST'])
def api_fields(request):
    if request.method == "GET":
        fields = Field.objects.all()
        data = [{"id": field.id, "name": field.name} for field in fields]
        return JsonResponse({
            "fields": data
        })
    else:
        data = json.loads(request.body)
        field = Field.objects.create(name=data["name"])
        return JsonResponse({
            "id": field.id,
            "name": field.name
        })


@require_http_methods(['GET', 'POST'])
def api_matches(request):
    if request.method == "GET":
        matches = Match.objects.all()
        data = [get_match_details_helper(match) for match in matches]
        return JsonResponse({
            "matches": data
        })
    else:
        data = json.loads(request.body)
        if Player.objects.filter(id=data["player1_id"]).exists():
            p1 = Player.objects.get(id=data["player1_id"])
        else:
            return HttpResponseBadRequest("Bad request: You tried to create a match with a player that doesn't exist yet.")

        if Player.objects.filter(id=data["player2_id"]).exists():
            p2 = Player.objects.get(id=data["player2_id"])
        else:
            return HttpResponseBadRequest("Bad request: You tried to create a match with a player that doesn't exist yet.")

        if Field.objects.filter(id=data["field_id"]).exists():
            field = Field.objects.get(id=data["field_id"])
        else:
            return HttpResponseBadRequest("Bad request: You tried to create a match with a player that doesn't exist yet.")

        match = Match.objects.create(
            date_and_time=datetime.datetime.now(),
            player1=p1,
            player2=p2,
            player1_score=data["player1_score"],
            player2_score=data["player2_score"],
            field=field
        )
        return JsonResponse({
            "id": match.id,
            "date_and_time": match.date_and_time,
            "player1": match.player1.name,
            "player2": match.player2.name,
            "player1_score": match.player1_score,
            "player2_score": match.player2_score,
            "field": match.field.name
        })

def get_match_details_helper(match):
    return {
        "id": match.id,
        "date_and_time": match.date_and_time,
        "player1": match.player1.name,
        "player2": match.player2.name,
        "player1_score": match.player1_score,
        "player2_score": match.player2_score,
        "field": match.field.name
    }


@require_GET
def api_player_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return JsonResponse({
        "id": player.id,
        "name": player.name
    })


@require_GET
def api_field_detail(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    return JsonResponse({
        "id": field.id,
        "name": field.name
    })


@require_GET
def api_match_detail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return JsonResponse({
        "id": match.id,
        "date_and_time": match.date_and_time,
        "player1": match.player1.name,
        "player2": match.player2.name,
        "player1_score": match.player1_score,
        "player2_score": match.player2_score,
        "field": match.field.name
    })
