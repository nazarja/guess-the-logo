from app import app
from flask import render_template, redirect, url_for, session, request
from app.forms import LoginForm
from app.helpers import get_leaderboard



#=====================#

# index
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    # new instance of LoginForm
    login_form = LoginForm()
    session['url'] = 'home'

    # login in user
    if login_form.validate_on_submit():
        session['user'] = login_form.username.data

    # default - render index.html
    return render_template('index.html', login_form=login_form)


#=====================#


# leaderboard
@app.route('/leaderboard')
def leaderboard():
    leaderboard = get_leaderboard()
    session['url'] = 'leaderboard'
    return render_template('leaderboard.html', leaderboard=leaderboard)


#=====================#


# logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


#=====================#