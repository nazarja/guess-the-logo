import os
from app import app

# run app   
app.run(host=os.environ.get('IP', '0.0.0.0'), port=os.environ.get('PORT', '5000'), debug=False)
# app.run(debug=True)

