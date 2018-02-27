import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods


from .models import Player, Field, Match
from .helpers import get_match_details, remove_invalid_matches, create_new_match


def index(request):
    matches = Match.objects.all()
    players = Player.objects.all()
    fields = Field.objects.all()
    field_ids = [field.id for field in fields]
    player_ids = [player.id for player in players]
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
        'player_ids': player_ids,
        'field_ids': field_ids,
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


@require_POST
def new_player_form(request):
    data = request.POST
    Player.objects.create(name=data["name"])
    return redirect('players')


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
        data = [get_match_details(match) for match in matches]
        return JsonResponse({
            "matches": data
        })
    else:
        data = json.loads(request.body)
        try:
            create_new_match(data["player1"], data["player2"], data["player1_score"], data["player2_score"], data["field"])
            return redirect('main')
        except KeyError:
            return HttpResponse("Whoopsie. You tried to create a match with some invalid ids for players and/or field")


@require_POST
def new_match_form(request):
    data = request.POST
    try:
        create_new_match(data["player1"], data["player2"], data["player1_score"], data["player2_score"], data["field"])
        return redirect('main')
    except ObjectDoesNotExist:
        return HttpResponse("Nope. Can't do that. Wrong player and/or field id. Object does not exist")


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
    return JsonResponse(get_match_details(match))


@require_POST
def api_remove_invalid_matches(request):
    response = remove_invalid_matches()
    return JsonResponse(json.dumps(response), safe=False)
