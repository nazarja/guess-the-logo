from app import app
from flask import render_template, redirect, url_for, session, request, flash
from app.forms import LoginForm, AnswerForm
from app.helpers import get_leaderboard,  login_user, create_session_variables, reset_variables



#=====================#

# index
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    if 'user' in session:
        # reset variables
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

    session['index'] += 1
    answer_form = AnswerForm()

    print(session['game'][session['index']]['answer'])
    print(answer_form.answer.data)
    
    if answer_form.validate_on_submit():
        pass
    
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