from app import app
from flask import render_template
from app.forms import LoginForm



#=====================#

# index
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    # new instance of LoginForm
    login_form = LoginForm()

    #
    if login_form.validate_on_submit():
        pass

    # default - rentrun index.html
    return render_template('index.html', login_form=login_form)


#=====================#