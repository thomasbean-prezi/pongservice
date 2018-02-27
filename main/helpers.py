from .models import Player, Field, Match


def get_invalid_match_ids():
    matches = Match.objects.all()
    invalid_match_ids = [match.id for match in matches if is_match_invalid(match)]
    return invalid_match_ids


def is_match_invalid(match):
    score_list = [match.player2_score, match.player1_score]
    if score_list.count(11) == 1:
        return not (0 <= match.player1_score <= 11 and 0 <= match.player2_score <= 11)
    else:
        return True


def remove_invalid_matches():
    invalid_match_ids = get_invalid_match_ids()
    for match_id in invalid_match_ids:
        Match.objects.get(pk=match_id).delete()

    return invalid_match_ids


def get_match_details(match):
    return {
        "id": match.id,
        "date_and_time": match.date_and_time,
        "player1": match.player1.name,
        "player2": match.player2.name,
        "player1_score": match.player1_score,
        "player2_score": match.player2_score,
        "field": match.field.name
    }


def create_new_match(p1_id, p2_id, p1_score, p2_score, field_id):
    return Match.objects.create(
        player1=Player.objects.get(pk=p1_id),
        player2=Player.objects.get(pk=p2_id),
        player1_score=p1_score,
        player2_score=p2_score,
        field=Field.objects.get(pk=field_id)
    )


def construct_match_results_for_view():
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
    return context
