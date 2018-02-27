import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods


from .models import Player, Field, Match
from .helpers import get_match_details, remove_invalid_matches, create_new_match, construct_match_results_for_view


def index(request):
    context = construct_match_results_for_view()
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
        try:
            data = json.loads(request.body)
            player = Player.objects.create(name=data["name"])
            return JsonResponse({
                "id": player.id,
                "name": player.name
            })
        except ValueError:
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
        try:
            data = json.loads(request.body)
            try:
                create_new_match(data["player1"], data["player2"], data["player1_score"], data["player2_score"], data["field"])
                return redirect('main')
            except KeyError:
                return HttpResponse("Whoopsie. You tried to create a match with some invalid ids for players and/or field")
        except ValueError:
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
