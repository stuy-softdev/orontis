# Leon Wong
# Software Development
# September 2026
# COLLABORATORS: Darren Lin, Saxon Rassner
# TEAMNAME: We are the best best best best at Python and Software Development

'''
PREDICTIONS
Running app.py will start a Flask server; the hello_world() function will run and "No hablo queso!" will be displayed

ACTUAL
Flask server started on localhost, "No hablo queso!" displayed on webpage.
'''

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()


