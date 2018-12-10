import json, time, math 
from random import shuffle
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from datetime import datetime

	
#============================================#


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


			# add new user to leaderboard
			add_to_leaderboard(user['username'])

			# seek file to overwrite
			# Add new user to the users_file
			# return the new user
			users_file.seek(0)
			json.dump(users, users_file)
			return user

	
#============================================#


def add_to_leaderboard(username):
	with open('app/data/leaderboard.json', 'r+') as leaderboard_file:
		leaderboard = json.load(leaderboard_file)

		user = {
			"username": username,
			"best_time": 0, 
			"best_score": 0, 
			"best_rating": 0, 
		}
		leaderboard['users'].append(user)

		leaderboard_file.seek(0)
		json.dump(leaderboard, leaderboard_file)

	
#============================================#


def get_leaderboard():
	with open('app/data/leaderboard.json', 'r+') as leaderboard_file:
		leaderboard = json.load(leaderboard_file)

		if 'user' in session:
		# if the user is already on the leaderboard
		# and they hav a new best score
		# update the users record
			for user in leaderboard['users']:
				if session['user'] == user['username']:
					if session['best_rating'] > user['best_rating']:
						user['best_time'] = session['best_time']
						user['best_score'] = session['best_score']
						user['best_rating'] = session['best_rating']
						break
			leaderboard_file.seek(0)
			json.dump(leaderboard, leaderboard_file)


			# Add current user scores to leaderboard - only if its not their first time playing
			# but dont write to file - this is for seeing last played scores
			# against best scores
			if session['times_played'] > 0 and session['current_rating'] != 0:
				current_user = {
					"username": "LAST PLAYED",
					"best_time": session['current_time'], 
					"best_score": session['current_score'], 
					"best_rating": session['current_rating'], 
				}
				leaderboard['users'].append(current_user)


		# lamda learned from w3resource.com
		leaderboard['users'].sort(key=lambda x: x['best_rating'], reverse=True)
		return leaderboard['users']

	
#============================================#

       
def get_game():
    with open('app/data/game.json') as game_file:
        game = json.load(game_file)
        shuffle(game['game'])
        return game['game']

	
#============================================#


def reset_variables():
	session['game'] = get_game()
	session['index'] = 0
	session['current_time'] = 0
	session['current_score'] = 0
	session['current_rating'] = 0
	session['new_game'] = 1

	
#============================================#


def create_session_variables(user):
	session['user'] = user['username']
	session['last_played'] = user['last_played']
	session['times_played'] = user['times_played']
	session['best_time'] = user['best_time']
	session['best_score'] = user['best_score']
	session['best_rating'] = user['best_rating']

	
#============================================#


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

	
#============================================#


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

	
#============================================#




