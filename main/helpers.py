from .models import Player, Field, Match


def get_invalid_matches():
    matches = Match.objects.all()
    invalid_matches = [match for match in matches if is_match_invalid(match)]
    return invalid_matches


def is_match_invalid(match):
    score_list = [match.player2_score, match.player1_score]
    if score_list.count(11) == 1:
        if  0 <= match.player1_score <= 11 or 0 <= match.player2_score <= 11:
            return False
        else:
            return True
    else:
        return True


def remove_invalid_matches():
    invalid_matches = get_invalid_matches()
    for match in invalid_matches:
        match.delete()


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
