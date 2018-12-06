import json


def get_leaderboard():
    with open('app/data/leaderboard.json') as leaderboard_file:
        leaderboard = json.load(leaderboard_file)
        return leaderboard['leaderboard']