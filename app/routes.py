from app import app
from flask import render_template, redirect, url_for, session, request, flash
from app.forms import LoginForm, AnswerForm
from app.helpers import get_leaderboard,  login_user, create_session_variables, reset_variables, set_session_scores
import time



#=====================#

# index
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    # reset variables
    if 'user' in session:
        reset_variables()

    # new instance of LoginForm
    login_form = LoginForm()

    # if form is valid
    if login_form.validate_on_submit():
        # check if user already exists and if password is correct
        user = login_user(login_form.username.data, login_form.password.data)
        
        # if False is return then password is incorrect
        if not user:
            flash('Incorrect username or password')
            return redirect(url_for('index'))
        else:
            create_session_variables(user)
            return redirect(url_for('index'))
        
    # default - render index.html
    return render_template('index.html', login_form=login_form, endpoint="index")


#=====================#


# game
@app.route('/game', methods=['GET', 'POST'])
def game():

    # protect route
    if not 'user' in session:
        return redirect(url_for('index'))

    # initialise form
    answer_form = AnswerForm()
    
    # check submitted answer
    if answer_form.validate_on_submit():
        # if answer is correct
        if session['game'][session['index'] - 1]['answer'] ==  answer_form.answer.data.lower():
            session['correct'] += 1
        else:
            if not answer_form.answer.data:
                # if answer is empty
                flash(f'answer field cannot be empty')
            else:
                # if answer is wrong
                flash(f'Incorrect answer! You guessed {answer_form.answer.data}, try again..')

            # return the same question
            # prevent index increasing
            session['index'] -= 1
            return redirect(url_for('game'))

    # If the game is over
    # Write users scores to file
    # redirect to leaderboard
    if session['index'] >= 2:
        set_session_scores()
        return redirect(url_for('leaderboard'))

    # increase index pagination
    session['index'] += 1

    
    # default - render game.html
    return render_template('game.html', endpoint="game", answer_form=answer_form)


#=====================#


# leaderboard
@app.route('/leaderboard')
def leaderboard():

    # new instance of Leaderboard
    leaderboard = get_leaderboard()
    return render_template('leaderboard.html', leaderboard=leaderboard, endpoint="leaderboard")


#=====================#


# logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


#=====================#