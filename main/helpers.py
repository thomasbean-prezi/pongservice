from .models import Player, Field, Match


def get_invalid_matches():
    matches = Match.objects.all()
    invalid_matches = []
    for match in matches:
        if match.player1_score != 11 and match.player2_score != 11:
            invalid_matches.append(match)
            continue

        if match.player1_score == 11 and match.player2_score == 11:
            invalid_matches.append(match)
            continue

        if match.player1_score > 11 or match.player2_score > 11:
            invalid_matches.append(match)
            continue

        if match.player1_score < 0 or match.player2_score < 0:
            invalid_matches.append(match)
            continue

    return invalid_matches


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

def get_initials(name):
    if name.strip() == "":
        return ""

    name_parts = name.split(" ")
    letters = [part[0] + "." for part in name_parts]
    return " ".join(letters)
