import json, random



'''
    open json file and parse to dict,
    use lamda function to sort by rating,
    reverse will order by highest rating
'''

def get_leaderboard():
    with open('app/data/leaderboard.json') as leaderboard_file:
        leaderboard = json.load(leaderboard_file)
        leaderboard_list = leaderboard['leaderboard']

        # lamda learned from w3resource.com
        leaderboard_list.sort(key=lambda x: x['rating'], reverse=True)
        return leaderboard_list


        
def get_game():
    with open('app/data/game.json') as game_file:
        game = json.load(game_file)
        random.shuffle(game['game'])
        return game['game']
