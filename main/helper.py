
from .models import *


def get_invalid_matches():
    matches = Match.objects.all()
    invalid_matches = []
    for match in matches:
        if(match.player1_score != 11 and match.player2_score != 11):
            invalid_matches.append(match)
            continue

        if(match.player1_score > 11 or match.player2_score > 11):
            invalid_matches.append(match)
            continue

        if(match.player1_score < 0 or match.player2_score < 0):
            invalid_matches.append(match)
            continue

    return(invalid_matches)

def remove_invalid_matches():
    invalid_matches = get_invalid_matches()
    for match in invalid_matches:
        match.delete()
