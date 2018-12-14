import os
from app import app

# run app   
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=os.environ.get('PORT', '5000'))

