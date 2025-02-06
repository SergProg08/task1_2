from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

# pprint(game_stamps)

def get_score(game_stamps, offset):
    left, right = 0, len(game_stamps) - 1
    last_known_score = {"home": 0, "away": 0}

    while left <= right:
        mid = (left + right) // 2
        if game_stamps[mid]["offset"] == offset:
            return game_stamps[mid]["score"]["home"], game_stamps[mid]["score"]["away"]
        elif game_stamps[mid]["offset"] < offset:
            last_known_score = game_stamps[mid]["score"]
            left = mid + 1
        else:
            right = mid - 1

    
    return last_known_score["home"], last_known_score["away"]

def get_offset():
    while True:
        try:
            offset = int(input("Enter any offset: "))
        except ValueError:
            print("Please enter only an integer.")
        else: 
            return offset

print(get_score(game_stamps, get_offset()))

