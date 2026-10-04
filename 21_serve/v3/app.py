# Leon Wong
# Software Development
# September 2026
# COLLABORATORS: Darren Lin, Saxon Rassner
# TEAMNAME: We are the best best best best at Python and Software Development

'''
PREDICTIONS
Running app.py will start a Flask server; the hello_world() function will run.
The terminal should print: "about to print __name__...
__main__"

The browser should display: "No hablo queso!"

ACTUAL
Flask server started with debug mode on.
Visiting localhost still displayed "No hablo queso!" and the print statements still appeared in the terminal.
'''

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go?
    return "No hablo queso!"          #A: It will print to the terminal where the Flask server is running

app.debug = True
app.run()
