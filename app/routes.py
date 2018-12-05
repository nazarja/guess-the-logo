from app import app
from flask import render_template



#=====================#

# index
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    # default - rentrun index.html
    return render_template('index.html')


#=====================#