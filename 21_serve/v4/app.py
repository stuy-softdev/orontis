# Leon Wong
# Software Development
# September 2026
# COLLABORATORS: Darren Lin, Saxon Rassner

'''
PREDICTIONS
Running app.py directly will make __name__ equal "__main__", so the
if statement will be true. Debug mode will turn on and the Flask server
will start.

The terminal should print: "about to print __name__...
__main__"

The browser should display: "No hablo queso!"

ACTUAL
Running app.py directly started the Flask server with debug mode on.
Visiting localhost displayed "No hablo queso!" in the browser, while
the print statements appeared in the terminal.
'''

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
