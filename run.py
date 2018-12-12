import os
from app import app

# run app and set debug on
if __name__ == '__main__':
    # app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'))
    app.run(debug=True)