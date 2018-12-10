import json, random
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session


def login_user(username, password):  
	with open('app/data/users.json', 'r+') as users_file:
		users = json.load(users_file)

		# check for existing user
		for user in users['users']:
			# check if username exists
			if user['username'] == username.lower():
				# check hashed password matches submitted form password
				if check_password_hash(user['password'], password):
					# if True return user
					return user
				# if password is incorrect
				return False

		# if no user is found, create a new user
		# save username and password
		with open('app/data/user.json') as user_file:
			user = json.load(user_file)
			user['username'] = username.lower()
			user['password'] = generate_password_hash(password)
			users['users'].append(user)

			# seek file to overwrite
			# Add new user to the users_file
			# return the new user
			users_file.seek(0)
			json.dump(users, users_file)
			return user




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




def create_session_variables(user):
	session['user'] = user['username']
	session['last_played'] = user['last_played']
	session['times_played'] = user['times_played']
	session['best_time'] = user['best_time']
	session['best_score'] = user['best_score']
	session['rating'] = user['rating']
	session['current_time'] = user['current_time']
	session['current_score'] = user['current_score']
	session['current_rating'] = user['current_rating']




def reset_variables():
	session['game'] = get_game()
	session['index'] = 0
	session['correct'] = 0
	session['current_time'] = 0
	session['current_score'] = 0
	session['current_rating'] = 0
