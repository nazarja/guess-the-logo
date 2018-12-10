import json, time, math 
from random import shuffle
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from datetime import datetime




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
        shuffle(game['game'])
        return game['game']


def reset_variables():
	session['game'] = get_game()
	session['index'] = 0
	session['current_time'] = 0
	session['current_score'] = 0
	session['current_rating'] = 0
	session['new_game'] = 1



def create_session_variables(user):
	session['user'] = user['username']
	session['last_played'] = user['last_played']
	session['times_played'] = user['times_played']
	session['best_time'] = user['best_time']
	session['best_score'] = user['best_score']
	session['best_rating'] = user['best_rating']



def set_session_scores():
	# must convert datetime to string - cannot serialize datetime to JSON
	session['last_played'] = datetime.strftime(datetime.utcnow(), '%a, %d %b, %H:%M') 
	session['times_played'] += 1
	session['current_time'] = round(time.time() - session['start_time'])
	
	session['current_rating'] = (session['current_score'] * 1000) - (session['current_time'] * 10)
	print(session['current_rating'])

	if session['best_rating'] < session['current_rating']:
		session['best_time'] = session['current_time']
		session['best_score'] = session['current_score']
		session['best_rating'] = session['current_rating']
	
	# write new data to user dict for next login
	write_new_scores()

	

def write_new_scores():
	with open('app/data/users.json', 'r+') as users_file:
		users = json.load(users_file)
		
		for user in users['users']:
			if session['user'] == user['username']:
				user['last_played'] = session['last_played']
				user['times_played'] = session['times_played']
				user['best_time'] = session['best_time']
				user['best_score'] = session['best_score']
				user['best_rating'] = session['best_rating']
				break

		# overwrite users file with updated data
		users_file.seek(0)
		json.dump(users, users_file)



