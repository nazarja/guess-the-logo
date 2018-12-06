from app import app
from flask import render_template, redirect, url_for
from app.forms import LoginForm
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
        pass

    # default - render index.html
    return render_template('index.html', login_form=login_form)


#=====================#


# leaderboard
@app.route('/leaderboard')
def leaderboard():
    leaderboard = get_leaderboard()
    return render_template('leaderboard.html', leaderboard=leaderboard)


#=====================#


# logout
@app.route('/logout')
def logout():
    return redirect(url_for('index'))


#=====================#