from app import app
from flask import render_template, redirect, url_for, session, request
from app.forms import LoginForm, AnswerForm
from app.helpers import get_leaderboard



#=====================#

# index
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    # new instance of LoginForm
    login_form = LoginForm()

    # login in user
    if login_form.validate_on_submit():
        session['user'] = login_form.username.data

    # default - render index.html
    return render_template('index.html', login_form=login_form, endpoint="index")


#=====================#


# game
@app.route('/game')
def game():
    answer_form = AnswerForm()
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